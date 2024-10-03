import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetAssociatedFamilyParameters(dimension):
	if hasattr(dimension, "FamilyLabel"):
		if dimension.FamilyLabel != None: return dimension.FamilyLabel, dimension.FamilyLabel.Definition.Name
		else: return None, None
	else: return None, None

dimensions = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetAssociatedFamilyParameters(x) for x in dimensions]))
else: OUT = GetAssociatedFamilyParameters(dimensions)