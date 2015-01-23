import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
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
			itemlist.append(doc.GetElement(insert).ToDSType(True))
	except:
		donothing = 1
	elementlist.append(itemlist)
OUT = elementlist