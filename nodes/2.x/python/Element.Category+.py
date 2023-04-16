import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetCategory(item):
	if not item: return None, None
	objtype = item.GetType().ToString()
	if objtype == "Autodesk.Revit.DB.ParameterFilterElement": return [GetCategoryObjects(x) for x in item.GetCategories()]
	elif objtype == "Autodesk.Revit.DB.ViewSchedule": return GetCategoryObjects(item.Definition.CategoryId)
	elif objtype == "Autodesk.Revit.DB.Family": return GetCategoryObjects(item.FamilyCategoryId)
	elif objtype == "Autodesk.Revit.DB.GraphicsStyle":  return GetCategoryObjects(item.GraphicsStyleCategory.Id)
	elif objtype == "Revit.Application.Document":
		if item.IsFamilyDocument: 
			clr.AddReference("RevitServices")
			import RevitServices
			from RevitServices.Persistence import DocumentManager
			return GetCategoryObjects(DocumentManager.Instance.CurrentDBDocument.OwnerFamily.FamilyCategoryId)
		else: return None, None
	elif objtype == "Autodesk.Revit.DB.Category": 
		if item.Parent: return GetCategoryObjects(item.Parent.Id)
		else: return None, None
	elif hasattr(item, "Category"): 
		if item.Category: return GetCategoryObjects(item.Category.Id)
		else: return None, None
	else: return None, None

def GetCategoryObjects(catID):
	if not catID: return None, None
	returnBic = System.Enum.ToObject(BuiltInCategory, catID.IntegerValue)
	try: returnCat =  Revit.Elements.Category.ById(catID.IntegerValue)
	except: returnCat = None
	return returnCat, returnBic


items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetCategory(x) for x in items]))
else: OUT = GetCategory(items)