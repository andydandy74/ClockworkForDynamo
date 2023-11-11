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
	returnID = None
	returnIDs = None
	returnCat = None
	returnBic = None
	if objtype == "Autodesk.Revit.DB.ParameterFilterElement": returnIDs = item.GetCategories()
	elif objtype == "Autodesk.Revit.DB.ViewSchedule": returnID = item.Definition.CategoryId
	elif objtype == "Autodesk.Revit.DB.Family": returnID = item.FamilyCategoryId
	elif objtype == "Autodesk.Revit.DB.GraphicsStyle":  returnID = item.GraphicsStyleCategory.Id
	elif objtype == "Revit.Application.Document":
		if item.IsFamilyDocument: 
			clr.AddReference("RevitServices")
			import RevitServices
			from RevitServices.Persistence import DocumentManager
			returnID = DocumentManager.Instance.CurrentDBDocument.OwnerFamily.FamilyCategoryId
	elif objtype == "Autodesk.Revit.DB.Category": 
		if item.Parent: returnID = item.Parent.Id
	elif hasattr(item, "Category"): 
		if item.Category: returnID = item.Category.Id
	if returnID:
		returnBic = System.Enum.ToObject(BuiltInCategory, returnID.IntegerValue)
		try: returnCat =  Revit.Elements.Category.ById(returnID.IntegerValue)
		except: pass
	elif returnIDs:
		returnCat = []
		returnBic = []
		for returnID in returnIDs:
			returnBic.append(System.Enum.ToObject(BuiltInCategory, returnID.IntegerValue))
			try: returnCat.append(Revit.Elements.Category.ById(returnID.IntegerValue))
			except: returnCat.append(None)
		returnCat.sort()
	return returnCat, returnBic

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetCategory(x) for x in items]))
else: OUT = GetCategory(items)