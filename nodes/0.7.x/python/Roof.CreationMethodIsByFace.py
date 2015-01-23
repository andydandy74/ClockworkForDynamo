import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

roofinstances = UnwrapElement(IN[0])
booleans = list()
for item in roofinstances:
	try:
		if item.GetType().Name == 'RoofBase':
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans