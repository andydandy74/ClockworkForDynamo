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
		paramlist.append(dimension.FamilyLabel)
		paramnamelist.append(dimension.FamilyLabel.Definition.Name)
	except:
		paramlist.append(list())
		paramnamelist.append(list())
OUT = (paramlist,paramnamelist)