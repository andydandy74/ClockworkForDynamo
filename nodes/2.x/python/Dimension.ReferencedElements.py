import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetDimensionReferences(item):
	if hasattr(item, "References"):
		refs = []
		linkInstances = []
		for r in item.References:
			if r.LinkedElementId != ElementId.InvalidElementId: 
				if item.Document.GetElement(r.ElementId).GetLinkDocument():
					refs.append(item.Document.GetElement(r.ElementId).GetLinkDocument().GetElement(r.LinkedElementId))
				# if the link isn't loaded, just return the RevitLinkInstance instead of the actual element
				else: refs.append(item.Document.GetElement(r.ElementId))
				linkInstances.append(item.Document.GetElement(r.ElementId))
			else: 
				refs.append(item.Document.GetElement(r.ElementId))
				linkInstances.append(None)
		return refs, linkInstances		
	else: return None

dimensions = UnwrapElement(IN[0])

if isinstance(IN[0], list): 
	if len(IN[0]) > 0: OUT = list(zip(*[GetDimensionReferences(x) for x in dimensions]))
	else: OUT = [[],[]]
else: OUT = GetDimensionReferences(dimensions)