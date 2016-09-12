import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elementlist = list()

for item in items:
	itemlist = list()
	try:
		for subcomp in item.GetSubComponentIds():
			itemlist.append(item.Document.GetElement(subcomp).ToDSType(True))
	except:
		donothing = 1
	elementlist.append(itemlist)
OUT = elementlist