import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetSuperComponent(item):
	if hasattr(item, "SuperComponent"): return item.SuperComponent
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetSuperComponent(x) for x in items]
else: OUT = GetSuperComponent(items)