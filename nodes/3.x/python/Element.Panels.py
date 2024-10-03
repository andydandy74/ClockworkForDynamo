import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetCurtainPanels(host):
	if hasattr(host, "CurtainGrid"):
		return GetCurtainPanelsByGrid(host.CurtainGrid, host)
	elif hasattr(host, "CurtainGrids"):
		return [GetCurtainPanelsByGrid(x, host) for x in host.CurtainGrids]
	else: return []

def GetCurtainPanelsByGrid(grid, host):
	if grid:
		if organizeInRows:
			uGrids = [ElementId.InvalidElementId]
			[uGrids.append(x) for x in grid.GetUGridLineIds()]
			vGrids = [ElementId.InvalidElementId]
			[vGrids.append(x) for x in grid.GetVGridLineIds()]
			panels = []
			for u in uGrids:
				row = []
				for v in vGrids:
					panel = grid.GetPanel(u,v)
					if hasattr(panel, "FindHostPanel"):
						hostpanelid = panel.FindHostPanel()
						if hostpanelid.IntegerValue != -1: panel = host.Document.GetElement(hostpanelid)
					row.append(panel)
				panels.append(row)
			return panels
		else:
			panellist = [host.Document.GetElement(x) for x in grid.GetPanelIds()]
			for panel in panellist:
				if hasattr(panel, "FindHostPanel"):
					hostpanelid = panel.FindHostPanel()
					if hostpanelid.IntegerValue != -1:
						panellist[panellist.index(panel)] = host.Document.GetElement(hostpanelid)
			return [x.ToDSType(True) for x in panellist]
	else: return list()

items = UnwrapElement(IN[0])
organizeInRows = IN[1]

if isinstance(IN[0], list): OUT = [GetCurtainPanels(x) for x in items]
else: OUT = GetCurtainPanels(items)