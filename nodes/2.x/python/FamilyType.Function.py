import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetFunction(item):
	try: return item.get_Parameter(BuiltInParameter.FUNCTION_PARAM).AsValueString()
	except: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetFunction(x) for x in items]
else: OUT = GetFunction(items)