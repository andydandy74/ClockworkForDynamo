import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
assemblies = UnwrapElement(IN[0])
elementlist = list()

# disassemble assemblies
TransactionManager.Instance.EnsureInTransaction(doc)
for assinst in assemblies:
	memberslist = assinst.Disassemble()
	members = list()
	for item in memberslist:
		members.append(doc.GetElement(item))
	elementlist.append(members)
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist