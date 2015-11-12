import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

elements = UnwrapElement(IN[0])
cat = UnwrapElement(IN[1])
elementlist = list()
for item in elements:
	if item.Category.Id==cat.Id:
		elementlist.append(True)
	else:
		elementlist.append(False)
OUT = elementlist