import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetCurtainGridLines(host):
	if hasattr(host, "CurtainGrid"):
		return GetCurtainGridLinesByGrid(host.CurtainGrid, host)
	elif hasattr(host, "CurtainGrids"):
		return map(list, zip(*[GetCurtainGridLinesByGrid(x, host) for x in host.CurtainGrids]))	
	else: return []

def GetCurtainGridLinesByGrid(grid, host):
	if grid:
		uGrids = [host.Document.GetElement(x) for x in grid.GetUGridLineIds()]
		vGrids = [host.Document.GetElement(x) for x in grid.GetVGridLineIds()]
		return uGrids, vGrids
	else: return list()

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCurtainGridLines(x) for x in items]
else: OUT = GetCurtainGridLines(items)