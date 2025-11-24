import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetRoofCreationMethod(item):
	if not item: return None
	elif item.GetType().Name == 'FootPrintRoof': return 'By Footprint'
	elif item.GetType().Name == 'ExtrusionRoof': return 'By Extrusion'
	elif item.GetType().Name == 'RoofBase': return 'By Face'
	elif item.GetType().Name == 'FamilyInstance': return 'In-Place'
	else: return None

roofs = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetRoofCreationMethod(x) for x in roofs]
else: OUT = GetRoofCreationMethod(roofs)