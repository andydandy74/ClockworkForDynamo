import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
booleans = list()

for view in views:
	if str(view.ViewType) == 'Section':
		booleans.append(True)
	else:
		booleans.append(False)
OUT = booleans		