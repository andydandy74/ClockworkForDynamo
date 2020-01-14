import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def CollectByView(bic, view):
	collector = FilteredElementCollector(doc)
	filter = ElementOwnerViewFilter(view.Id)
	return collector.WherePasses(filter).OfCategory(bic).ToElements()

def GetViewDependentElements(cat, views):
	if isinstance(views, list): return [CollectByView(cat, x) for x in UnwrapElement(views)]
	else: return CollectByView(cat, UnwrapElement(views))

doc = DocumentManager.Instance.CurrentDBDocument
cats = IN[0]
views = IN[1]

if isinstance(IN[0], list): OUT = [GetViewDependentElements(x, views) for x in cats]
else: OUT = GetViewDependentElements(cats, views)