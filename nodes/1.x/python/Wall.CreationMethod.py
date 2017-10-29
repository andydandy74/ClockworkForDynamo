import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

wallinstances = UnwrapElement(IN[0])
methodlist = list()
for item in wallinstances:
	typename = item.GetType().Name
	if typename == 'Wall':
		methodlist.append('Standard')
	elif typename == 'FaceWall':
		methodlist.append('By Face')
	elif typename == 'FamilyInstance':
		methodlist.append('In-Place')
	else: methodlist.append(None)
OUT = methodlist