import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
elementlist = list()

for item in items:
	try: 
		if item.SlabShapeEditor.SlabShapeCreases.IsEmpty == True or item.SlabShapeEditor.SlabShapeVertices.IsEmpty == True:
			elementlist.append(False)
		else:
			elementlist.append(True)
	except:
		elementlist.append(False)
OUT = elementlist