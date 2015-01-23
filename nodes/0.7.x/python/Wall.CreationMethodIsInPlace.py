import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

wallinstances = UnwrapElement(IN[0])
booleans = list()
for item in wallinstances:
	try:
		if item.GetType().Name == 'FamilyInstance':
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans