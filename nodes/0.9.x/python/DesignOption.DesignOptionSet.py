import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

desopts = UnwrapElement(IN[0])
elementlist = list()
for item in desopts:
	elementlist.append(item.Document.GetElement(item.get_Parameter(BuiltInParameter.OPTION_SET_ID).AsElementId()))
OUT = elementlist