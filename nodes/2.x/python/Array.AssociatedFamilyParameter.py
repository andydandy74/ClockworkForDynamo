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
	if basearray.GetType().ToString() in ("Autodesk.Revit.DB.LinearArray", "Autodesk.Revit.DB.RadialArray"):
		if basearray.Label != None:
			paramlist.append(basearray.Label)
			paramnamelist.append(basearray.Label.Definition.Name)
		else:
			paramlist.append(None)
			paramnamelist.append(None)
	else:
		paramlist.append(None)
		paramnamelist.append(None)
OUT = (paramlist,paramnamelist)