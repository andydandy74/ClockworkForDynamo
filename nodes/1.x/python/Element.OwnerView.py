import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetOwnerView(item):
	if hasattr(item, "OwnerViewId"): return item.Document.GetElement(item.OwnerViewId)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetOwnerView(x) for x in items]
else: OUT = GetOwnerView(items)