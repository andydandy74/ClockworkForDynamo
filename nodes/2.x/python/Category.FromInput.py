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

def GetCatFromInput(var):	
	if var:
		cattype = var.GetType().ToString()
		if cattype == "Autodesk.Revit.DB.Category": return var
		elif cattype == "Autodesk.Revit.DB.BuiltInCategory": return Category.GetCategory(doc, var)
		elif cattype == "System.String": 
			found = [x for x in bics if x.ToString() == var]
			if len(found) > 0: return Category.GetCategory(doc, found[0])	
		else: return None			
	else: return None

doc = DocumentManager.Instance.CurrentDBDocument
bics = System.Enum.GetValues(BuiltInCategory)
cats = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCatFromInput(x) for x in cats]
else: OUT = GetCatFromInput(cats)