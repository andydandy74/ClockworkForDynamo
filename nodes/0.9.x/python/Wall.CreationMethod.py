import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

wallinstances = UnwrapElement(IN[0])
methodlist = list()
for item in wallinstances:
	try:
		if item.GetType().Name == 'Wall':
			methodlist.append('Standard')
		elif item.GetType().Name == 'FaceWall':
			methodlist.append('By Face')
		elif item.GetType().Name == 'FamilyInstance':
			methodlist.append('In-Place')
		else:
			methodlist.append('No Wall')
	except:
		methodlist.append('No Wall')
OUT = methodlist