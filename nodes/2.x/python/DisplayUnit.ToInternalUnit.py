import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def ToInternalUnits(val, unittype):
	if str(dispunit.GetType()) == "Autodesk.Revit.DB.DisplayUnitType":
		return UnitUtils.ConvertToInternalUnits(val,unittype)
	else: return None

vals = IN[0]
dispunit = IN[1]

if isinstance(IN[0], list): OUT = [ToInternalUnits(x, dispunit) for x in vals]
else: OUT = ToInternalUnits(vals, dispunit)