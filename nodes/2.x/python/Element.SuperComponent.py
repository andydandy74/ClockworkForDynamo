import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetSuperComponent(item):
	# nested families
	if hasattr(item, "SuperComponent"): return item.SuperComponent
	# beam systems
	if hasattr(item, "BeamBelongsTo"): return BeamSystem.BeamBelongsTo(item)
	# handrails
	if hasattr(item, "HostRailingId"): return item.Document.GetElement(item.HostRailingId)
	# stair components
	elif hasattr(item, "GetStairs"): return item.GetStairs()
	# site subregions
	elif hasattr(item, "IsSiteSubRegion"):
		if item.IsSiteSubRegion:
			return item.Document.GetElement(item.AsSiteSubRegion().HostId)
	# grid segments
	elif item.GetType().ToString() == 'Autodesk.Revit.DB.Grid': 
		sc = MultiSegmentGrid.GetMultiSegementGridId(item)
		if sc: return item.Document.GetElement(sc)
		else: return None
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetSuperComponent(x) for x in items]
else: OUT = GetSuperComponent(items)