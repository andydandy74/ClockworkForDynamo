import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsRelatedToMass(item):
	try:
		if item.get_Parameter(BuiltInParameter.RELATED_TO_MASS).AsInteger() == 1:
			return True
		else: return False
	except: return False

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsRelatedToMass(x) for x in items]
else: OUT = IsRelatedToMass(items)