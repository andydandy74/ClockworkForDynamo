import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
elementlist = list()

for view in views:
	elementlist.append(str(view.ViewType))
OUT = elementlist