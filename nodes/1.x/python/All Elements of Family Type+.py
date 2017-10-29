import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

famtypes = UnwrapElement(IN[0])
inputdoc = UnwrapElement(IN[2])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

elementlist = list()
for ft in famtypes:
	collector = FilteredElementCollector(doc)
	bic = System.Enum.ToObject(BuiltInCategory, ft.Category.Id.IntegerValue)
	collector.OfCategory(bic)
	elementlist.append([x for x in collector.ToElements() if x.GetTypeId().IntegerValue == ft.Id.IntegerValue])
OUT = elementlist