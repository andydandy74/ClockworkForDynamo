import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetWorkset(item):
	if hasattr(item, "WorksetId"): return item.Document.GetWorksetTable().GetWorkset(item.WorksetId)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetWorkset(x) for x in items]
else: OUT = GetWorkset(items)