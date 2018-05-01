import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetPlacementType(item):
	if hasattr(item, "FamilyPlacementType"): return item.FamilyPlacementType
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetPlacementType(x) for x in items]
else: OUT = GetPlacementType(items)