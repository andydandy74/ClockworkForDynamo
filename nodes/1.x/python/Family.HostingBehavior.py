import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fams = UnwrapElement(IN[0])
hosttypes = list()
for fam in fams:
	if fam.GetType().ToString() == "Autodesk.Revit.DB.Family":
		hosttypes.append(fam.get_Parameter(BuiltInParameter.FAMILY_HOSTING_BEHAVIOR).AsValueString())
	else: hosttypes.append(None)
OUT = hosttypes