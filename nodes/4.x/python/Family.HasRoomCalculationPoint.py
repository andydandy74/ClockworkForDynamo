import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def HasRCP(fam):
	if fam.GetType().ToString() == "Autodesk.Revit.DB.Family":
		return fam.get_Parameter(BuiltInParameter.ROOM_CALCULATION_POINT).AsInteger() == 1
	else: return False

fams = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [HasRCP(x) for x in fams]
else: OUT = HasRCP(fams)