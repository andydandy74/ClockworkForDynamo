import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetGroup(item):
	if hasattr(item, "GroupId"): return item.Document.GetElement(item.GroupId)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetGroup(x) for x in items]
else: OUT = GetGroup(items)