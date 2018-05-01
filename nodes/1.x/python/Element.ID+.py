import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetId(item):
	if hasattr(item, "Id"): return item.Id.IntegerValue
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetId(x) for x in items]
else: OUT = GetId(items)