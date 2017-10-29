import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

desopts = UnwrapElement(IN[0])
elementlist = list()
for item in desopts:
	elementlist.append(item.Document.GetElement(item.get_Parameter(BuiltInParameter.OPTION_SET_ID).AsElementId()).ToDSType(True))
OUT = elementlist