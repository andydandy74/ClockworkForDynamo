import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsCategoryVisibleInView(cat, view, version):
	if version > 2016:
		if view.GetCategoryHidden(cat.Id): return False
		else: return True
	else:
		if view.GetVisibility(cat): return True
		else: return False

cats = IN[0]
views = UnwrapElement(IN[1])

if isinstance(IN[0], list):
	if isinstance(IN[1], list):  OUT = [[IsCategoryVisibleInView(x, y, IN[2]) for x in cats] for y in views]
	else: OUT = [IsCategoryVisibleInView(x, views, IN[2]) for x in cats]
else:
	if isinstance(IN[1], list): OUT = [IsCategoryVisibleInView(cats, x, IN[2]) for x in views]
	else: OUT = IsCategoryVisibleInView(cats, views, IN[2])