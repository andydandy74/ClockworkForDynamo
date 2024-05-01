import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])

def GetCopingElements(item):
	if hasattr(item, "GetCopingIds"): return [item.Document.GetElement(x) for x in item.GetCopingIds()]
	else: return []

if isinstance(IN[0], list): OUT = [GetCopingElements(x) for x in items]
else: OUT = GetCopingElements(items) 