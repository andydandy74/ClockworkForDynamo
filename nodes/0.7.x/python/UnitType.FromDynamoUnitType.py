import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

dynunittype = IN[0]
if str(dynunittype) == 'DynamoUnits.Area':
	ut = UnitType.UT_Area
elif str(dynunittype) == 'DynamoUnits.Length':
	ut = UnitType.UT_Length
elif str(dynunittype) == 'DynamoUnits.Volume':
	ut = UnitType.UT_Volume
else:
	ut = null
OUT = ut