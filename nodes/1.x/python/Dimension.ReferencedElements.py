import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetDimensionReferences(item):
	if hasattr(item, "References"):
		return [item.Document.GetElement(x.ElementId) for x in item.References]
	else: return None

dimensions = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetDimensionReferences(x) for x in dimensions]
else: OUT = GetDimensionReferences(dimensions)