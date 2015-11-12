import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

walltypes = UnwrapElement(IN[0])
functionlist = list()

for item in walltypes:
	try:
		functionlist.append(item.get_Parameter(BuiltInParameter.FUNCTION_PARAM).AsValueString())
	except:
		functionlist.append('No Wall/Function')
OUT = functionlist