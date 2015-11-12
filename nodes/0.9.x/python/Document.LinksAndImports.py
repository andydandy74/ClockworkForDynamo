import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
# need to learn how to implement LINQ here...
collector = FilteredElementCollector(doc)
impinst = collector.OfClass(ImportInstance).ToElements()
linkedlist = list()
importlist = list()
for item in impinst:
	if item.IsLinked:
		linkedlist.append(item)
	else:
		importlist.append(item)
OUT = (linkedlist,importlist)