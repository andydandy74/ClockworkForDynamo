import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def ElementTypesByCategory(cat, doc):
	bic = System.Enum.ToObject(BuiltInCategory, cat.Id)
	collector = FilteredElementCollector(doc).OfCategory(bic).WhereElementIsElementType()
	return collector.ToElements()

inputdoc = UnwrapElement(IN[2])
if not inputdoc: doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document": doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument

if isinstance(IN[0], list): OUT = [ElementTypesByCategory(x, doc) for x in IN[0]]
else: OUT = ElementTypesByCategory(IN[0], doc)