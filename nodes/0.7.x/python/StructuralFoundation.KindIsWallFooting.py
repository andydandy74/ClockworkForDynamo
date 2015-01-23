import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

foundinstances = UnwrapElement(IN[0])
booleans = list()
for item in foundinstances:
	try:
		if item.GetType().Name == 'ContFooting':
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans