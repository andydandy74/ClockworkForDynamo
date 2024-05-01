import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

def GetHandOrientation(item):
	if hasattr(item, "HandOrientation"): return item.HandOrientation.ToVector()
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetHandOrientation(x) for x in items]
else: OUT = GetHandOrientation(items)