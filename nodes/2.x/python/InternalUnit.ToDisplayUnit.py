import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def FromInternalUnits(val, unittype):
	if (version > 2021 and str(dispunit.GetType()) == "Autodesk.Revit.DB.ForgeTypeId") or (version < 2022 and str(dispunit.GetType()) == "Autodesk.Revit.DB.DisplayUnitType"):
		return UnitUtils.ConvertFromInternalUnits(val,unittype)
	else: return None

vals = IN[0]
dispunit = IN[1]
version = IN[2]

if isinstance(IN[0], list): OUT = [FromInternalUnits(x, dispunit) for x in vals]
else: OUT = FromInternalUnits(vals, dispunit)