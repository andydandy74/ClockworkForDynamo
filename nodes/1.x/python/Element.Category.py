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
		elementlist.append(Revit.Elements.Category.ById(item.Category.Id.IntegerValue))
	except:
		# Is it a schedule
		try:
			elementlist.append(Revit.Elements.Category.ById(item.Definition.CategoryId.IntegerValue))
		except:
			elementlist.append(None)

OUT = elementlist