import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetMass(item):
	if hasattr(item, "OwningMassId"): return item.Document.GetElement(item.OwningMassId).ToDSType(True)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetMass(x) for x in items]
else: OUT = GetMass(items)