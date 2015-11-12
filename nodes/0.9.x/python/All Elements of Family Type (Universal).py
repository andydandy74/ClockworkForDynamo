import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
famtypes = UnwrapElement(IN[0])

elementlist = list()
for ft in famtypes:
	collector = FilteredElementCollector(doc)
	bic = System.Enum.ToObject(BuiltInCategory, ft.Category.Id.IntegerValue)
	collector.OfCategory(bic)
	# This is a workaround
	# because I was to lazy to learn
	# how to implement LINQ in Python
	ftlist =  list()
	for item in collector.ToElements():
		if item.GetTypeId().IntegerValue == ft.Id.IntegerValue:
			ftlist.append(item)
	elementlist.append(ftlist)
OUT = elementlist