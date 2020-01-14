import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])

def IsMirrored(item):
	if hasattr(item, "Mirrored"):
		return item.Mirrored
	else: return False


if isinstance(IN[0], list): OUT = [IsMirrored(x) for x in items]
else: OUT = IsMirrored(items)