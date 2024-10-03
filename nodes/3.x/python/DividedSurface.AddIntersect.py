import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
divsurf = UnwrapElement(IN[0])
intersects = UnwrapElement(IN[1])

TransactionManager.Instance.EnsureInTransaction(doc)
for item in intersects:
	divsurf.AddIntersectionElement(item.Id)
TransactionManager.Instance.TransactionTaskDone()

OUT = divsurf