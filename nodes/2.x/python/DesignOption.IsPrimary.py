import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def DesignOptionIsPrimary(item):
	if hasattr(item, "IsPrimary"): return item.IsPrimary
	else: return False

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [DesignOptionIsPrimary(x) for x in items]
else: OUT = DesignOptionIsPrimary(items)