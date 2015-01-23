import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
booleans = list()
for item in items:
	try:
		if item.CurtainGrids:
			booleans.append(False)
		else:
			booleans.append(True)
	except:
		booleans.append(False)
OUT = booleans