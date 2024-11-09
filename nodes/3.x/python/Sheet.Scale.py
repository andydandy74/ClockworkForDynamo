import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetSheetScale(sheet):
	if hasattr(sheet, "Scale"): return sheet.get_Parameter(BuiltInParameter.SHEET_SCALE).AsValueString()
	else: return None

sheets = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = [GetSheetScale(x) for x in sheets]
else: OUT = GetSheetScale(sheets)