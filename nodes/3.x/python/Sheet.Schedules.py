import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetSheetSchedules(sheet):
	if hasattr(sheet, "SheetNumber"):
		viewlist = list()
		collector = FilteredElementCollector(sheet.Document, sheet.Id).OfClass(ScheduleSheetInstance)
		return [sheet.Document.GetElement(x.ScheduleId) for x in collector]
	else: return list()
	
sheets = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetSheetSchedules(x) for x in sheets]
else: OUT = GetSheetSchedules(sheets)