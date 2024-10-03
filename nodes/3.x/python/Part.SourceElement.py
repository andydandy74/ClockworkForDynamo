import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetPartSource(part):
	if hasattr(part, "GetSourceElementIds"):
		return [part.Document.GetElement(x.HostElementId).ToDSType(True) for x in part.GetSourceElementIds()]
	else: return list()

parts = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetPartSource(x) for x in parts]
else: OUT = GetPartSource(parts)