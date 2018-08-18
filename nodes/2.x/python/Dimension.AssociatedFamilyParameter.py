import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

dimensions = UnwrapElement(IN[0])
paramlist = list()
paramnamelist = list()
for dimension in dimensions:
	try:
		if dimension.FamilyLabel != None:
			paramlist.append(dimension.FamilyLabel)
			paramnamelist.append(dimension.FamilyLabel.Definition.Name)
		else:	
			paramlist.append(None)
			paramnamelist.append(None)
	except:
		paramlist.append(None)
		paramnamelist.append(None)
OUT = (paramlist,paramnamelist)