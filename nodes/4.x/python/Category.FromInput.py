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
		if isinstance(var, str): 
			try: return Category.GetCategory(doc, eval("BuiltInCategory." + var))
			except: return None
		elif isinstance(var, int): return Category.GetCategory(doc, var)
		else:
			cattype = var.GetType().ToString()
			if cattype == "Autodesk.Revit.DB.Category": return var
			elif cattype == "Autodesk.Revit.DB.BuiltInCategory": return Category.GetCategory(doc, var)
			else: return None
	else: return None

doc = DocumentManager.Instance.CurrentDBDocument
cats = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCatFromInput(x) for x in cats]
else: OUT = GetCatFromInput(cats)