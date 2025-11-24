import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import System

def GetCurveType(item):
	if hasattr(item, "CurveElementType"): return System.Enum.GetName(CurveElementType, item.CurveElementType)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCurveType(x) for x in items]
else: OUT = GetCurveType(items)