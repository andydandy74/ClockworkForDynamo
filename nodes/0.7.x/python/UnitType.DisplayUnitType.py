import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

unittype = IN[0]
doc = DocumentManager.Instance.CurrentDBDocument
formatoptions = doc.GetUnits().GetFormatOptions(unittype)
dispunits = formatoptions.DisplayUnits
symtype = formatoptions.UnitSymbol
if symtype == UnitSymbolType.UST_NONE:
	dispsym = 'None'
else:
	dispsym = LabelUtils.GetLabelFor(symtype)
OUT = (dispunits,dispsym)