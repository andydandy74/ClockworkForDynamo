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
		sublist = []
		for subcat in cat.SubCategories:
			sublist.append(Revit.Elements.Category.ById(subcat.Id.IntegerValue))
		elementlist.append(sublist)
	except:
		elementlist.append(list())
OUT = elementlist