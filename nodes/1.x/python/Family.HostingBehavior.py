import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetHostingBehavior(item):
	if item.GetType().ToString() == "Autodesk.Revit.DB.Family":
		hb = item.get_Parameter(BuiltInParameter.FAMILY_HOSTING_BEHAVIOR).AsValueString()
		if hb == "": return None
		else: return hb
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetHostingBehavior(x) for x in items]
else: OUT = GetHostingBehavior(items)