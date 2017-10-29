import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

cats = IN[0]
inputdoc = UnwrapElement(IN[2])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

elementlist = list()
for item in cats:
	collector = FilteredElementCollector(doc)
	collector.OfClass(FamilySymbol)
	bic = System.Enum.ToObject(BuiltInCategory, item.Id)
	collector.OfCategory(bic)
	elementlist.append(collector.ToElements())
OUT = elementlist