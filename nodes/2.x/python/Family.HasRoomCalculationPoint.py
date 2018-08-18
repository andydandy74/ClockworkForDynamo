import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fams = UnwrapElement(IN[0])
booleans = list()
for fam in fams:
	if fam.GetType().ToString() == "Autodesk.Revit.DB.Family":
		booleans.append(fam.get_Parameter(BuiltInParameter.ROOM_CALCULATION_POINT).AsInteger() == 1)
		#booleans.append(fam.get_Parameter(BuiltInParameter.ROOM_CALCULATION_POINT).AsInteger())
	else: booleans.append(False)
OUT = booleans