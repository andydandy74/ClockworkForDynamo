import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	try:
		elementlist.append(item.Id.IntegerValue)
	except:
		elementlist.append(None)
OUT = elementlist