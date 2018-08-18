import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetFoundationKind(item):
	if not item: return None
	elif item.GetType().Name == 'FamilyInstance': return 'Isolated'
	elif item.GetType().Name == 'WallFoundation': return 'Wall Footing'
	elif item.GetType().Name == 'Floor': return 'Slab'
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetFoundationKind(x) for x in items]
else: OUT = GetFoundationKind(items)