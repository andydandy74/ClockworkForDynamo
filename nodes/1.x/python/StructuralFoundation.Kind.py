import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

foundinstances = UnwrapElement(IN[0])
kindlist = list()
for item in foundinstances:
	try:
		if item.GetType().Name == 'FamilyInstance':
			kindlist.append('Isolated')
		elif item.GetType().Name == 'WallFoundation':
			kindlist.append('Wall Footing')
		elif item.GetType().Name == 'Floor':
			kindlist.append('Slab')
		else: kindlist.append('No Foundation')
	except:
		kindlist.append('No Foundation')
OUT = kindlist