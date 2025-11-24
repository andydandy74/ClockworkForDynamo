import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def GetBicFromInput(var):	
	if var:
		if isinstance(var, str): 
			try:
				eval("BuiltInCategory." + var)
				return var
			except: return None
		elif isinstance(var, int): return System.Enum.GetName(BuiltInCategory, var)
		else:
			cattype = var.GetType().ToString()
			if cattype == "Revit.Elements.Category": return System.Enum.GetName(BuiltInCategory, var.Id)
			elif cattype == "Autodesk.Revit.DB.BuiltInCategory": return var
			else: return None
	else: return None

doc = DocumentManager.Instance.CurrentDBDocument

if isinstance(IN[0], list): OUT = [GetBicFromInput(x) for x in IN[0]]
else: OUT = GetBicFromInput(IN[0])