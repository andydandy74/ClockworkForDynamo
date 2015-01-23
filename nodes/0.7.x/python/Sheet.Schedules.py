import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
sheets = UnwrapElement(IN[0])
elementlist = list()

for sheet in sheets:
	try:
		viewlist = list()
		collector = FilteredElementCollector(doc, sheet.Id).OfClass(ScheduleSheetInstance)
		for item in collector:
			viewlist.append(doc.GetElement(item.ScheduleId))
		elementlist.append(viewlist)
	except:
		elementlist.append(list())
OUT = elementlist