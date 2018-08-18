import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
	selsetmembers = list()
	for member in item.GetElementIds():
		selsetmembers.append(item.Document.GetElement(member))
	elementlist.append(selsetmembers)
OUT = elementlist