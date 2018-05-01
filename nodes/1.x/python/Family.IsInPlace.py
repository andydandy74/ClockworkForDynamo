import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsInPlace(item):
	if hasattr(item, "IsInPlace"): return item.IsInPlace
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsInPlace(x) for x in items]
else: OUT = IsInPlace(items)