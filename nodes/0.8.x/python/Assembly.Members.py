import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
assemblies = UnwrapElement(IN[0])
elementlist = list()

for assinst in assemblies:
	memberslist = assinst.GetMemberIds()
	members = list()
	for item in memberslist:
		members.append(doc.GetElement(item))
	elementlist.append(members)

OUT = elementlist