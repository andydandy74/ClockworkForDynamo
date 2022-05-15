import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def GetAssociatedFamilyParameters(element):
	paramlist = list()
	assoclist = list()
	paramnamelist = list()
	assocnamelist = list()
	try:
		for param in element.Parameters:
			assoc = doc.FamilyManager.GetAssociatedFamilyParameter(param)
			if assoc != None:
				paramlist.append(param)
				assoclist.append(assoc)
				paramnamelist.append(param.Definition.Name)
				assocnamelist.append(assoc.Definition.Name)
	except: pass
	return paramlist,assoclist,paramnamelist,assocnamelist

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetAssociatedFamilyParameters(x) for x in items]))
else: OUT = GetAssociatedFamilyParameters(items)