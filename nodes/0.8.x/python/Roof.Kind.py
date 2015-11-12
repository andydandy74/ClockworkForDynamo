import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	try:
		if item.CurtainGrids:
			elementlist.append('Glazed')
		else:
			elementlist.append('Basic')
	except:
		elementlist.append('Other / No Roof')
OUT = elementlist