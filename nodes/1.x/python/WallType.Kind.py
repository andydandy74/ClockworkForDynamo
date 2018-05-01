import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def WallTypeKind(walltype):
	if hasattr(walltype,"Kind"): return str(walltype.Kind)
	else: return None

walltypes = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [WallTypeKind(x) for x in walltypes]
else: OUT = WallTypeKind(walltypes)