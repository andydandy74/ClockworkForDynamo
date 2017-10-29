import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fams = UnwrapElement(IN[0])
ptypes = list()
for fam in fams:
	if fam.GetType().ToString() == "Autodesk.Revit.DB.Family":
		ptypes.append(fam.FamilyPlacementType)
	else: ptypes.append(None)
OUT = ptypes