import clr

items = IN[0]
elementlist = list()

try:
	clr.AddReference('RevitAPI')
	from Autodesk.Revit.DB import *
	for item in items:
		elementlist.append(dir(UnwrapElement(item)))
except:
	for item in items:
		elementlist.append(dir(item))
OUT = elementlist