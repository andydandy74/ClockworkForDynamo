import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetSelSetMembers(selset):
	if hasattr(selset, "GetElementIds"): return [selset.Document.GetElement(x) for x in selset.GetElementIds()]
	else: return list()

selsets = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetSelSetMembers(x) for x in selsets]
else: OUT = GetSelSetMembers(selsets)