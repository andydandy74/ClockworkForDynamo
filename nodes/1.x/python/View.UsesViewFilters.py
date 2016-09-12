import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])
elementlist = list()

collector = FilteredElementCollector(doc)
filters = collector.OfClass(FilterElement).ToElements()

for view in views:
	try:
		thisfilter = False
		for filter in filters:
			if view.IsFilterApplied(filter.Id):
				thisfilter = True
		if thisfilter:
			elementlist.append(True)
		else:
			elementlist.append(False)
	except:
		elementlist.append(False)
OUT = elementlist