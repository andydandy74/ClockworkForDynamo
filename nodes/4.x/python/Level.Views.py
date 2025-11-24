import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

import System
from System.Collections.Generic import *

def GetFirstAndAllViews(lvl):
	firstView = None
	try:
		if lvl.Document.GetElement(lvl.FindAssociatedPlanViewId()): firstView = lvl.Document.GetElement(lvl.FindAssociatedPlanViewId())
	except: pass
	if viewlevels.Contains(lvl.Id): allViews = views[viewlevels.IndexOf(lvl.Id)]
	else: allViews = []
	return firstView, allViews

levels = UnwrapElement(IN[0])
views = UnwrapElement(IN[1])
viewlevels = List[ElementId]([x.Id for x in UnwrapElement(IN[2])])

if isinstance(IN[0], list): OUT = list(zip(*[GetFirstAndAllViews(x) for x in levels]))
else: OUT = GetFirstAndAllViews(levels)