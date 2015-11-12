import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
elementlist = list()

for view in views:
	try:
		if view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId().IntegerValue == -1:
			elementlist.append(list())
		else:
			elementlist.append(view.Document.GetElement(view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId()))
	except:
		elementlist.append(list())
OUT = elementlist