import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
groups = UnwrapElement(IN[0])
elementlist = list()
TransactionManager.Instance.EnsureInTransaction(doc)
for group in groups:
	try:
		ids = group.UngroupMembers()
		ungrouped = list()
		for id in ids:
			ungrouped.append(group.Document.GetElement(id))
		elementlist.append(ungrouped)
	except:
		elementlist.append(list())
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist