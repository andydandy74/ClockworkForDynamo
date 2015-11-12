import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])
views = UnwrapElement(IN[1])

elementlist = list()
# This could be more elegant if only I knew how to implement a Multicategory filter in Python....
for e in elements:
	elist = list()
	for view in views:
		vlist = list()
		collector = FilteredElementCollector(doc)
		filter = ElementOwnerViewFilter(view.Id)
		bic = System.Enum.ToObject(BuiltInCategory, e.Category.Id.IntegerValue)
		for item in collector.WherePasses(filter).OfCategory(bic).ToElements():
			if item.GetTypeId().IntegerValue == e.GetTypeId().IntegerValue:
				vlist.append(item)
		elist.append(vlist)
	elementlist.append(elist)
OUT = elementlist