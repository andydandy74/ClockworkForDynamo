import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
elementlist = list()
for view in views:
	try:
		elementlist.append(str(view.DetailLevel))
	except:
		elementlist.append('Undefined')
OUT = elementlist