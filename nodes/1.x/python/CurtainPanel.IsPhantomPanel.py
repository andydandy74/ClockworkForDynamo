import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsPhantomPanel(item):
	try: 
		if item.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).HasValue: return False
		else: return True
	except: return False

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsPhantomPanel(x) for x in items]
else: OUT = IsPhantomPanel(items)