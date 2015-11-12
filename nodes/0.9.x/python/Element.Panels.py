import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	try:
		if item.CurtainGrid is None:
			elementlist.append(list())
		else:
			panellist = list()
			for panel in item.CurtainGrid.GetPanelIds():
				panellist.append(item.Document.GetElement(panel).ToDSType(True))
			elementlist.append(panellist)
	except:
		elementlist.append(list())
OUT = elementlist