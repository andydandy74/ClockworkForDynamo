import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

massfloors = UnwrapElement(IN[0])
elementlist = list()
for item in massfloors:
	try:
		elementlist.append(item.Document.GetElement(item.OwningMassId).ToDSType(True))
	except:
		elementlist.append(None)
OUT = elementlist