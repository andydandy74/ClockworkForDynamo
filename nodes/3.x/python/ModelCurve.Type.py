import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetCurveType(item):
	if hasattr(item, "CurveElementType"): return item.CurveElementType
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCurveType(x) for x in items]
else: OUT = GetCurveType(items)