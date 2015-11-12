import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

walltypes = UnwrapElement(IN[0])
kindlist = list()
for item in walltypes:
	try: 
		kindlist.append(str(item.Kind))
	except:
		kindlist.append('No Wall')
OUT = kindlist