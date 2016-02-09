import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	paramlist = list()
	assoclist = list()
	paramnamelist = list()
	assocnamelist = list()
	try:
		for param in item.Parameters:
			assoc = doc.FamilyManager.GetAssociatedFamilyParameter(param)
			if assoc != None:
				paramlist.append(param)
				assoclist.append(assoc)
				paramnamelist.append(param.Definition.Name)
				assocnamelist.append(assoc.Definition.Name)
	except:
		pass
	elementlist.append((paramlist,assoclist,paramnamelist,assocnamelist))
OUT = elementlist