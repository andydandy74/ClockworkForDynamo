import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

cats = UnwrapElement(IN[0])
elementlist = list()

for cat in cats:
	try:
		elementlist.append(cat.SubCategories)
	except:
		elementlist.append(list())
OUT = elementlist