import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])

def GetSubComponents(item):
	# FamilyInstances
	if hasattr(item, "GetSubComponentIds"):
		return [item.Document.GetElement(x) for x in item.GetSubComponentIds()]
	# Stairs
	elif hasattr(item, "GetStairsLandings"):
		stair_comps = [item.Document.GetElement(x) for x in item.GetStairsLandings()]
		stair_comps.extend([item.Document.GetElement(x) for x in item.GetStairsRuns()])
		stair_comps.extend([item.Document.GetElement(x) for x in item.GetStairsSupports()])
		return stair_comps
	# Railings
	elif hasattr(item, "GetHandRails"):
		rail_comps = [item.Document.GetElement(x) for x in item.GetHandRails()]
		rail_comps.append(item.Document.GetElement(item.TopRail))
		return rail_comps
	# Beam systems
	elif hasattr(item, "GetBeamIds"):
		return [item.Document.GetElement(x) for x in item.GetBeamIds()]
	else: return []

if isinstance(IN[0], list): OUT = [GetSubComponents(x) for x in items]
else: OUT = GetSubComponents(items)