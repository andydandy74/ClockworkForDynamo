import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

vals = IN[0]
dispunit = IN[1]
elementlist = []
for val in vals:
	elementlist.append(UnitUtils.ConvertFromInternalUnits(val,dispunit))
OUT = elementlist