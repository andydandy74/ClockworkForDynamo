import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

inputdoc = UnwrapElement(IN[0])
if not inputdoc: doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document": doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument
cats = IN[2]

collector = FilteredElementCollector(doc).OfClass(Family)
items = collector.ToElements()

def ReturnIfCategory(items, cat):
	if cat: return [x for x in items if x.FamilyCategory.Id.IntegerValue == cat.Id.IntegerValue]
 	else: return []

if isinstance(cats, list): OUT = [ReturnIfCategory(items, x) for x in cats]
else: OUT = ReturnIfCategory(items, cats)