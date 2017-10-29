import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

roofinstances = UnwrapElement(IN[0])
elementlist = list()
for item in roofinstances:
	if item.GetType().Name == 'FootPrintRoof': elementlist.append('By Footprint')
	elif item.GetType().Name == 'ExtrusionRoof': elementlist.append('By Extrusion')
	elif item.GetType().Name == 'RoofBase': elementlist.append('By Face')
	elif item.GetType().Name == 'FamilyInstance': elementlist.append('In-Place')
	else: elementlist.append(None)
OUT = elementlist