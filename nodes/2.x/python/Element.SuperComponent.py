import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetSuperComponent(item):
	if hasattr(item, "SuperComponent"): 
		sc = item.SuperComponent
		if sc: return sc
		else: return BeamSystem.BeamBelongsTo(item)
	if hasattr(item, "HostRailingId"): return item.Document.GetElement(item.HostRailingId)
	elif hasattr(item, "GetStairs"): return item.GetStairs()
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetSuperComponent(x) for x in items]
else: OUT = GetSuperComponent(items)