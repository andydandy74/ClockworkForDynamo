import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

viewsheetsets = UnwrapElement(IN[0])
elementlist = list()
for set in viewsheetsets:
	views = list()
	for view in set.Views:
		views.append(view)
	elementlist.append(views)
OUT = elementlist