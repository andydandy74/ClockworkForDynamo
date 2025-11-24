import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetGPFormula(gp):
	if hasattr(gp, "GetFormula"): return gp.GetFormula()
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetGPFormula(x) for x in items]
else: OUT = GetGPFormula(items)