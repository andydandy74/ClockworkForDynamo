import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])

elementlist = list()
for e in elements:
	collector = FilteredElementCollector(doc)
	bic = System.Enum.ToObject(BuiltInCategory, e.Category.Id.IntegerValue)
	collector.OfCategory(bic)
	# This is a workaround
	# because I was to lazy to learn
	# how to implement LINQ in Python
	elist =  list()
	for item in collector.ToElements():
		if item.GetTypeId().IntegerValue == e.GetTypeId().IntegerValue:
			elist.append(item)
	elementlist.append(elist)
OUT = elementlist