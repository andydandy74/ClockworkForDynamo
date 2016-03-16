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
		famlabel = dimension.FamilyLabel
		labelname = famlabel.Definition.Name
	except:
		famlabel = list()
		labelname = list()
	paramlist.append(famlabel)
	paramnamelist.append(labelname)
OUT = (paramlist,paramnamelist)