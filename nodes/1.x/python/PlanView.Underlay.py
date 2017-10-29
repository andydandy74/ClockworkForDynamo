import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
baselvl = []
toplvl = []
ulOrientation = []

for view in views:
	# Revit 2016 R2 and later
	try:
		if view.GetUnderlayBaseLevel().IntegerValue == -1:
			baselvl.append(None)
		else:
			baselvl.append(view.Document.GetElement(view.GetUnderlayBaseLevel()))
		if view.GetUnderlayTopLevel().IntegerValue == -1:
			toplvl.append(None)
		else:
			toplvl.append(view.Document.GetElement(view.GetUnderlayTopLevel()))
		ulOrientation.append(str(view.GetUnderlayOrientation()))
	# anything before
	except:
		toplvl.append(None)
		ulOrientation.append(None)
		try:
			if view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId().IntegerValue == -1:
				baselvl.append(None)
			else:
				baselvl.append(view.Document.GetElement(view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId()))
		except:
			baselvl.append(None)
OUT = (baselvl,toplvl,ulOrientation)