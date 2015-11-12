import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

sheets = UnwrapElement(IN[0])
elementlist = list()
for item in sheets:
	try:
		elementlist.append(item.get_Parameter(BuiltInParameter.SHEET_SCALE).AsString())
	except:
		elementlist.append(False)
OUT = elementlist