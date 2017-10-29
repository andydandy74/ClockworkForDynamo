import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
functionlist = list()

for item in items:
	try:
		functionlist.append(item.get_Parameter(BuiltInParameter.FUNCTION_PARAM).AsValueString())
	except:
		functionlist.append(None)
OUT = functionlist