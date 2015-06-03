import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

unittype = IN[0]
doc = DocumentManager.Instance.CurrentDBDocument
dispunits = doc.GetUnits().GetFormatOptions(unittype).DisplayUnits
dispsym = LabelUtils.GetLabelFor(doc.GetUnits().GetFormatOptions(unittype).UnitSymbol)
OUT = (dispunits,dispsym)