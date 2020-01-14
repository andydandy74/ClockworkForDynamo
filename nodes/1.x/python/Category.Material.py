import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

cats = UnwrapElement(IN[0])

def GetCatMat(cat):
	if hasattr(cat, "Material"): 
		try: return cat.Material.ToDSType(True)
		except: return None
	else: return None

if isinstance(IN[0], list): OUT = [GetCatMat(x) for x in cats]
else: OUT = GetCatMat(cats)