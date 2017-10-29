import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
elementlist = list()
notaview = list()
for view in views:
	try:
		if view.IsTemplate:
			elementlist.append(True)
		else:
			elementlist.append(False)
	except:
		elementlist.append(False)
OUT = elementlist