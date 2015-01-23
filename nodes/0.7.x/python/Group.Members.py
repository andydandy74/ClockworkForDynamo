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
groups = UnwrapElement(IN[0])
elementlist = list()
for item in groups:
	try:
		memberlist = list()
		for member in item.GetMemberIds():
			memberlist.append(doc.GetElement(member))
		elementlist.append(memberlist)
	except:
		elementlist.append(list())
OUT = elementlist