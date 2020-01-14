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
	bic = None
	if var:
		cattype = var.GetType().ToString()
		if cattype == "Revit.Elements.Category": bic = System.Enum.ToObject(BuiltInCategory, var.Id)
		elif cattype == "Autodesk.Revit.DB.BuiltInCategory": bic = var
		elif cattype == "System.String": 
			found = [x for x in bics if x.ToString() == var]
			if len(found) > 0: bic = found[0]
	return bic

doc = DocumentManager.Instance.CurrentDBDocument
bics = System.Enum.GetValues(BuiltInCategory)

if isinstance(IN[0], list): OUT = [GetBicFromInput(x) for x in IN[0]]
else: OUT = GetBicFromInput(IN[0])