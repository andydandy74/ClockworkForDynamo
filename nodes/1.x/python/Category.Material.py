import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

cats = UnwrapElement(IN[0])
elementlist = list()

for cat in cats:
	try:
		elementlist.append(cat.Material.ToDSType(True))
	except:
		elementlist.append(None)
OUT = elementlist