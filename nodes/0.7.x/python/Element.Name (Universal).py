import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

faminsts = UnwrapElement(IN[0])
elementlist = list()
for item in faminsts:
	try:
		elementlist.append(item.Name)
	except:
		elementlist.append(list())
OUT = elementlist