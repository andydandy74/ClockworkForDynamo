import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	try:
		if item.CurtainGrid is None:
			elementlist.append(list())
		else:
			panellist = list()
			for panel in item.CurtainGrid.GetPanelIds():
				panellist.append(doc.GetElement(panel).ToDSType(True))
			elementlist.append(panellist)
	except:
		elementlist.append(list())
OUT = elementlist