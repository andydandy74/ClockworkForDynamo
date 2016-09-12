import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

faminsts = UnwrapElement(IN[0])
elementlist = list()
for item in faminsts:
	try:
		elementlist.append(item.Document.GetElement(item.FindHostPanel()).ToDSType(True))
	except:
		elementlist.append(list())
OUT = elementlist