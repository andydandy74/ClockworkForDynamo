import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
incopenings = IN[1]
incshadows = IN[2]
incwalls = IN[3]
incshared = IN[4]
elementlist = list()

for item in items:
	itemlist = list()
	try:
		for insert in item.FindInserts(incopenings,incshadows,incwalls,incshared):
			itemlist.append(item.Document.GetElement(insert).ToDSType(True))
	except:
		pass
	elementlist.append(itemlist)
OUT = elementlist