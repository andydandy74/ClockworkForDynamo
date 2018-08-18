import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetUnderlays(view):
	baselvl = None
	toplvl = None
	ulOrientation = None
	# Revit 2016 R2 and later
	if hasattr(view, "GetUnderlayBaseLevel"):	
		if view.GetUnderlayBaseLevel().IntegerValue > 0: baselvl = view.Document.GetElement(view.GetUnderlayBaseLevel())
		if view.GetUnderlayTopLevel().IntegerValue > 0: toplvl = view.Document.GetElement(view.GetUnderlayTopLevel())
		ulOrientation = str(view.GetUnderlayOrientation())
	# anything before
	else:
		try: 
			if view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId().IntegerValue > 0: baselvl = view.Document.GetElement(view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId())
		except: pass
	return baselvl, toplvl, ulOrientation

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetUnderlays(x) for x in views]))
else: OUT = GetUnderlays(views)