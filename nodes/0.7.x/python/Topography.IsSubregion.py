import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

topos = UnwrapElement(IN[0])
booleans = list()
for item in topos:
	try:
		if item.IsSiteSubRegion:
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans