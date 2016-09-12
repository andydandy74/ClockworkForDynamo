import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

basearrays = UnwrapElement(IN[0])
paramlist = list()
paramnamelist = list()
for basearray in basearrays:
	try:
		if basearray.Label != None:
			paramlist.append(basearray.Label)
			paramnamelist.append(basearray.Label.Definition.Name)
	except:
		paramlist.append(list())
		paramnamelist.append(list())
OUT = (paramlist,paramnamelist)