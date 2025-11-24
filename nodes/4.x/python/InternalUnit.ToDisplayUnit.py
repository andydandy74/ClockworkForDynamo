import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def FromInternalUnits(val, unittype):
	if str(dispunit.GetType()) == "Autodesk.Revit.DB.ForgeTypeId":
		return UnitUtils.ConvertFromInternalUnits(val,unittype)
	else: return None

vals = IN[0]
dispunit = IN[1]

if isinstance(IN[0], list): OUT = [FromInternalUnits(x, dispunit) for x in vals]
else: OUT = FromInternalUnits(vals, dispunit)