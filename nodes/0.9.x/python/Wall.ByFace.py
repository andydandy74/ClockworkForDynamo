import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
walltype = UnwrapElement(IN[0])
locline = IN[1]
facerefs = IN[2]
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for ref in facerefs:
	try:
		newwall = FaceWall.Create(doc,walltype.Id,locline,ref)
		elementlist.append(newwall)
	except:
		elementlist.append(list())
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist