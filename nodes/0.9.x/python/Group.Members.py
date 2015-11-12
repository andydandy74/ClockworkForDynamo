import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

groups = UnwrapElement(IN[0])
elementlist = list()
for item in groups:
	try:
		memberlist = list()
		for member in item.GetMemberIds():
			memberlist.append(item.Document.GetElement(member))
		elementlist.append(memberlist)
	except:
		elementlist.append(list())
OUT = elementlist