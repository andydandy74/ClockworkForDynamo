import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
booleans = list()
for item in items:
	try:
		if item.get_Parameter(BuiltInParameter.RELATED_TO_MASS).AsInteger() == 1:
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans