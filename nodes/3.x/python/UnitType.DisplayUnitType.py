import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

dynunittype = IN[0]
if IN[1] > 2021:
	if str(dynunittype.GetType()) == "Autodesk.Revit.DB.ForgeTypeId":
		unittype = dynunittype
	elif str(dynunittype) == 'DynamoUnits.Area':
		unittype = ForgeTypeId('autodesk.spec.aec:area-2.0.0')
	elif str(dynunittype) == 'DynamoUnits.Length':
		unittype = ForgeTypeId('autodesk.spec.aec:length-2.0.0')
	elif str(dynunittype) == 'DynamoUnits.Volume':
		unittype = ForgeTypeId('autodesk.spec.aec:volume-2.0.0')
	else:
		unittype = None
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	dispunits = formatoptions.GetUnitTypeId()
	symtype = formatoptions.GetSymbolTypeId()
	if symtype.TypeId == '': dispsym = None
	else: dispsym = LabelUtils.GetLabelForSymbol(symtype)
else:
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
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	dispunits = formatoptions.DisplayUnits
	symtype = formatoptions.UnitSymbol
	if symtype == UnitSymbolType.UST_NONE: dispsym = None
	else: dispsym = LabelUtils.GetLabelFor(symtype)
OUT = (dispunits,dispsym)