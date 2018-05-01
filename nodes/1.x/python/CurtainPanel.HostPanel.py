import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetHostPanel(item):
	if hasattr(item, "FindHostPanel"):
		hpId = item.FindHostPanel()
		if hpId.IntegerValue > 0: return item.Document.GetElement(hpId).ToDSType(True)
		else: return item
	else: return item

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetHostPanel(x) for x in items]
else: OUT = GetHostPanel(items)