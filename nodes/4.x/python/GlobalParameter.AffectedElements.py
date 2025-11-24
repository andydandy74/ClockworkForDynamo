import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetAffectedElements(gp):
	if hasattr(gp, "GetAffectedElements"): 
		affected = []
		affected.extend([gp.Document.GetElement(x) for x in gp.GetAffectedElements()])
		affected.extend([gp.Document.GetElement(x) for x in gp.GetAffectedGlobalParameters()])
		affected.extend([gp.Document.GetElement(x) for x in gp.GetLabeledDimensions()])
		return affected
	else: return []

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetAffectedElements(x) for x in items]
else: OUT = GetAffectedElements(items)