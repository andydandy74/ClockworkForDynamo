import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

grouptypes = UnwrapElement(IN[0])
elementlist = list()
for gt in grouptypes:
	if gt.GetType().ToString() == "Autodesk.Revit.DB.GroupType":
		groups = gt.Groups
		glist = []
		for group in groups:
			glist.append(group.ToDSType(True))
		elementlist.append(glist)
	else: elementlist.append(List())
OUT = elementlist