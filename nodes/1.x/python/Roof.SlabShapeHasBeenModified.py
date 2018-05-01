import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def SlabShapeHasBeenModified(item):
	if hasattr(item, "SlabShapeEditor"):
		if item.SlabShapeEditor.SlabShapeCreases.IsEmpty == True or item.SlabShapeEditor.SlabShapeVertices.IsEmpty == True: return False
		else: return True
	else: return False

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [SlabShapeHasBeenModified(x) for x in items]
else: OUT = SlabShapeHasBeenModified(items)