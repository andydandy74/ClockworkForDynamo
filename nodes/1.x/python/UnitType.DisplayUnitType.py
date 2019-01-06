import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

dynunittype = IN[0]

if str(dynunittype.GetType()) == "Autodesk.Revit.DB.UnitType":
	unittype = dynunittype
elif str(dynunittype) == 'DynamoUnits.Area':
	unittype = UnitType.UT_Area
elif str(dynunittype) == 'DynamoUnits.Length':
	unittype = UnitType.UT_Length
elif str(dynunittype) == 'DynamoUnits.Volume':
	unittype = UnitType.UT_Volume
else:
	unittype = None

doc = DocumentManager.Instance.CurrentDBDocument
formatoptions = doc.GetUnits().GetFormatOptions(unittype)
dispunits = formatoptions.DisplayUnits
symtype = formatoptions.UnitSymbol
if symtype == UnitSymbolType.UST_NONE:
	dispsym = None
else:
	dispsym = LabelUtils.GetLabelFor(symtype)
OUT = (dispunits,dispsym)