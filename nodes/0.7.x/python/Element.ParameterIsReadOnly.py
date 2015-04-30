import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

element = UnwrapElement(IN[0])
params = IN[1]
elementlist = list()
for param in params:
	try:
		if element.Parameter[param].IsReadOnly:
			elementlist.append(True)
		else:
			elementlist.append(False)
	except:
		elementlist.append(False)
OUT = elementlist