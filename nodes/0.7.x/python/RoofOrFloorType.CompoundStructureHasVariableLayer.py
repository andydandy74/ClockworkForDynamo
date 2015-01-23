import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

elemtypes = UnwrapElement(IN[0])
elementlist = list()
for item in elemtypes:
	try:
		if item.GetCompoundStructure().VariableLayerIndex == -1:
			elementlist.append(False)
		else:
			elementlist.append(True)
	except:
		elementlist.append(False)
OUT = elementlist