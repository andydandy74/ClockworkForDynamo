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
		# Curtain systems
		systemlist = list()
		for grid in item.CurtainGrids:
			panellist = list()
			for panel in grid.GetPanelIds():
				panellist.append(item.Document.GetElement(panel).ToDSType(True))
			systemlist.append(panellist)
		elementlist.append(systemlist)
	except:
		try:
			# Curtain walls
			panellist = list()
			for panel in item.CurtainGrid.GetPanelIds():
				panellist.append(item.Document.GetElement(panel).ToDSType(True))
			elementlist.append(panellist)
		except:
			# Anything else
			elementlist.append(list())
OUT = elementlist