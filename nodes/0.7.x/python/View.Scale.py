import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
elementlist = list()
for view in views:
	try:
		elementlist.append(view.Scale)
	except:
		elementlist.append(list())
OUT = elementlist