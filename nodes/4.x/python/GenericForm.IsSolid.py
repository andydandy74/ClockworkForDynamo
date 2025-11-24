import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def CheckIfSolid(item):
	if hasattr(item, "IsSolid"): return item.IsSolid
	else: return None

items = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = [CheckIfSolid(x) for x in items]
else: OUT = CheckIfSolid(items)