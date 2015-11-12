import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

foundinstances = UnwrapElement(IN[0])
kindlist = list()
for item in foundinstances:
	try:
		if item.GetType().Name == 'FamilyInstance':
			kindlist.append('Isolated')
		elif item.GetType().Name == 'ContFooting':
			kindlist.append('Wall Footing')
		elif item.GetType().Name == 'Floor':
			kindlist.append('Slab')
	except:
		kindlist.append('No Foundation')
OUT = kindlist