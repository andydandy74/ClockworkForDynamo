import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	try:
		elementlist.append(item.StyleType.ToString())
	except:
		elementlist.append(list())
OUT = elementlist