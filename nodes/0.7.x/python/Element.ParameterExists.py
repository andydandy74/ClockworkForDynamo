import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
param = IN[1]
elementlist = list()
for item in items:
	try:
		if item.Parameter[param].GetType().Name == 'Parameter':
			elementlist.append(True)
		else:
			elementlist.append(False)
	except:
		elementlist.append(False)
OUT = elementlist