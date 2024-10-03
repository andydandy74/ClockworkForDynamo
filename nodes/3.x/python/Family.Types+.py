import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetFamilyTypes(fam):
	if hasattr(fam, "IsInPlace"):
		return [fam.Document.GetElement(x) for x in fam.GetFamilySymbolIds()]
	else: return []

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetFamilyTypes(x) for x in items]
else: OUT = GetFamilyTypes(items)