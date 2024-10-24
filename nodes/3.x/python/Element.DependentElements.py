import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])

def GetDependent(item):
	if hasattr(item, "GetDependentElements"): 
		return [item.Document.GetElement(x) for x in item.GetDependentElements(None) if x != item.Id]
	else: return []
	
if isinstance(IN[0], list): OUT = [GetDependent(x) for x in items]
else: OUT = GetDependent(items)