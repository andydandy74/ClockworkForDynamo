import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAssembly(item):
	if hasattr(item, "AssemblyInstanceId"): return item.Document.GetElement(item.AssemblyInstanceId)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetAssembly(x) for x in items]
else: OUT = GetAssembly(items)