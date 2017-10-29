import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

views = UnwrapElement(IN[0])
elementlist = list()
for view in views:
	try:
		elementlist.append(view.Document.GetElement(view.get_Parameter(BuiltInParameter.VIEW_PHASE).AsElementId()))
	except:
		elementlist.append(None)
OUT = elementlist