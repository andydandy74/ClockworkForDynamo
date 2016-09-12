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
		if item.Document.GetElement(item.GroupId) == None:
			elementlist.append(list())
		else:
			elementlist.append(item.Document.GetElement(item.GroupId))
	except:
		elementlist.append(list())
OUT = elementlist