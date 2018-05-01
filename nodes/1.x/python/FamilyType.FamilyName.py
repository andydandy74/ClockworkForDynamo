import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetFamilyName(item):
	if hasattr(item, "FamilyName"): return item.FamilyName
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetFamilyName(x) for x in items]
else: OUT = GetFamilyName(items)