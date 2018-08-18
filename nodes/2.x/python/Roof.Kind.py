import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetRoofKind(item):
	if hasattr(item, "CurtainGrids"):
		if item.CurtainGrids: return "Glazed"
		else: return "Basic"
	else: 
		if not item: return None
		elif item.GetType().Name == 'RoofBase': 
			if item.Document.GetElement(item.GetTypeId()).GetCompoundStructure(): return "Basic"
			else: return "Glazed"
		elif item.GetType().Name == 'FamilyInstance': return 'In-Place'
		else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetRoofKind(x) for x in items]
else: OUT = GetRoofKind(items)