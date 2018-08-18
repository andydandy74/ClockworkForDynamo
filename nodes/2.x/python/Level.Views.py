import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

levels = UnwrapElement(IN[0])
version = IN[1]
elementlist = list()
for lvl in levels:
	if version > 2017:
		try:
			if lvl.Document.GetElement(lvl.FindAssociatedPlanViewId()) == None:
				elementlist.append(None)
			else:
				elementlist.append(lvl.Document.GetElement(lvl.FindAssociatedPlanViewId()))
		except:
			elementlist.append(None)
	else:
		elementlist.append(None)
OUT = elementlist