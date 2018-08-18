import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetCategory(item):
	objtype = item.GetType().ToString()
	returnID = None
	if objtype == "Autodesk.Revit.DB.ViewSchedule": returnID = item.Definition.CategoryId
	elif objtype == "Autodesk.Revit.DB.Family": returnID = item.FamilyCategoryId
	elif objtype == "Autodesk.Revit.DB.GraphicsStyle":  returnID = item.GraphicsStyleCategory.Id
	elif objtype == "Autodesk.Revit.DB.Category": 
		if item.Parent: returnID = item.Parent.Id
	elif hasattr(item, "Category"): returnID = item.Category.Id
	if returnID:
		try: return Revit.Elements.Category.ById(returnID.IntegerValue)
		except: return None
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetCategory(x) for x in items]
else: OUT = GetCategory(items)