import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsEditable(item):
	if hasattr(item, "IsEditable"): return item.IsEditable
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsEditable(x) for x in items]
else: OUT = IsEditable(items)