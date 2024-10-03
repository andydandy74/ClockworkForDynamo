import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetMembers(item):
	if hasattr(item, "GetMemberIds"): return [item.Document.GetElement(x) for x in item.GetMemberIds()]
	else: return list()

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetMembers(x) for x in items]
else: OUT = GetMembers(items)