import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetCategoryType(cat):
	if hasattr(cat, "CategoryType"): return cat.CategoryType.ToString()
	else: return None

cats = UnwrapElement(IN[0])
elementlist = list()

if isinstance(IN[0], list): OUT = [GetCategoryType(x) for x in cats]
else: OUT = GetCategoryType(cats)