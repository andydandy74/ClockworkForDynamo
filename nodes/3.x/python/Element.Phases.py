import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetPhases(item):
	if hasattr(item, "CreatedPhaseId"):
		return item.Document.GetElement(item.CreatedPhaseId), item.Document.GetElement(item.DemolishedPhaseId)
	else: return None, None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetPhases(x) for x in items]))
else: OUT = GetPhases(items)