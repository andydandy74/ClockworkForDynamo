import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

walltypes = UnwrapElement(IN[0])
kindlist = list()
for item in walltypes:
	if item.GetType().ToString() == "Autodesk.Revit.DB.WallType":
		kindlist.append(str(item.Kind))
	else: kindlist.append(None)
OUT = kindlist