import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

sheets = UnwrapElement(IN[0])
elementlist = list()

for sheet in sheets:
	try:
		viewlist = list()
		collector = FilteredElementCollector(sheet.Document, sheet.Id).OfClass(ScheduleSheetInstance)
		for item in collector:
			viewlist.append(sheet.Document.GetElement(item.ScheduleId))
		elementlist.append(viewlist)
	except:
		elementlist.append(list())
OUT = elementlist