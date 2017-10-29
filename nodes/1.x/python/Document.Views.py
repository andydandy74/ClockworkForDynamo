import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

inputdoc = UnwrapElement(IN[1])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

collector = FilteredElementCollector(doc)
views = collector.OfClass(View).ToElements()
viewlist = list()
for view in views:
	if view.ViewType == ViewType.ThreeD:
		if not(view.IsTemplate):
			viewlist.append(view)
	else:
		viewlist.append(view)
OUT = viewlist