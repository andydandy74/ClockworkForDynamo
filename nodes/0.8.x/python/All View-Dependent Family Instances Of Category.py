import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
cats = IN[0]
views = UnwrapElement(IN[1])

elementlist = list()
# This could be more elegant if only I knew how to implement a Multicategory filter in Python....
for cat in cats:
	catlist = list()
	for view in views:
		collector = FilteredElementCollector(doc)
		filter = ElementOwnerViewFilter(view.Id)
		bic = System.Enum.ToObject(BuiltInCategory, cat.Id)
		catlist.append(collector.WherePasses(filter).OfCategory(bic).ToElements())
	elementlist.append(catlist)
OUT = elementlist