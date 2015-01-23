import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

walltypes = UnwrapElement(IN[0])
booleans = list()
for item in walltypes:
	try: 
		if str(item.Kind) == 'Curtain':
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans