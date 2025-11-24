import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def ElementsByCategory(bic, doc):
	if bic:
		collector = FilteredElementCollector(doc).OfCategory(eval("BuiltInCategory."+bic)).WhereElementIsNotElementType()
		return collector.ToElements()
	else: return []

inputdoc = UnwrapElement(IN[2])
if not inputdoc: doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document": doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument

if isinstance(IN[0], list): OUT = [ElementsByCategory(x, doc) for x in IN[0]]
else: OUT = ElementsByCategory(IN[0], doc)