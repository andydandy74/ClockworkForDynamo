import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

cats = UnwrapElement(IN[0])
views = UnwrapElement(IN[1])

elementlist = list()
for cat in cats:
	catlist = list()
	for view in views:
		try:
			if view.GetVisibility(cat):
				catlist.append(True)
			else:
				catlist.append(False)	
		except:
			catlist.append(False)
	elementlist.append(catlist)
OUT = elementlist