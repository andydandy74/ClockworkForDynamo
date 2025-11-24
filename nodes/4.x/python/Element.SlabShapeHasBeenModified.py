import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def SlabShapeHasBeenModified(item):
	sle = None
	if hasattr(item, "SlabShapeEditor"): sle = item.SlabShapeEditor
	elif hasattr(item, "GetSlabShapeEditor"): sle = item.GetSlabShapeEditor()
	else: return False
	if hasattr(sle, "SlabShapeCreases") and hasattr(sle, "SlabShapeVertices"):
		if sle.SlabShapeCreases.IsEmpty == True or sle.SlabShapeVertices.IsEmpty == True: return False
		else: return True
	else: return False

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [SlabShapeHasBeenModified(x) for x in items]
else: OUT = SlabShapeHasBeenModified(items)