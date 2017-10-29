import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	objtype = item.GetType().ToString()
	try:
		if objtype == "Autodesk.Revit.DB.ViewSchedule":
			elementlist.append(Revit.Elements.Category.ById(item.Definition.CategoryId.IntegerValue))
		elif objtype == "Autodesk.Revit.DB.Family":
			elementlist.append(Revit.Elements.Category.ById(item.FamilyCategoryId.IntegerValue))
		elif objtype == "Autodesk.Revit.DB.GraphicsStyle":
			elementlist.append(Revit.Elements.Category.ById(item.GraphicsStyleCategory.Id.IntegerValue))
		else:
			elementlist.append(Revit.Elements.Category.ById(item.Category.Id.IntegerValue))
	except:
		elementlist.append(None)

OUT = elementlist