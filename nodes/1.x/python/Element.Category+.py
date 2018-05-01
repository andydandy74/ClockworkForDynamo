import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetCategory(item):
	objtype = item.GetType().ToString()
	if objtype == "Autodesk.Revit.DB.ViewSchedule": return Revit.Elements.Category.ById(item.Definition.CategoryId.IntegerValue)
	elif objtype == "Autodesk.Revit.DB.Family": return Revit.Elements.Category.ById(item.FamilyCategoryId.IntegerValue)
	elif objtype == "Autodesk.Revit.DB.GraphicsStyle": return Revit.Elements.Category.ById(item.GraphicsStyleCategory.Id.IntegerValue)
	elif objtype == "Autodesk.Revit.DB.Category": 
		if item.Parent: return Revit.Elements.Category.ById(item.Parent.Id.IntegerValue)
		else: return None
	elif hasattr(item, "Category"): return Revit.Elements.Category.ById(item.Category.Id.IntegerValue)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCategory(x) for x in items]
else: OUT = GetCategory(items)