import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
ids = list()
rejects = list()
for item in items:
	try:
		ids.append(item.Id)
	except:
		rejects.append(item)
items = List[ElementId](ids)

TransactionManager.Instance.EnsureInTransaction(doc)
try:
	group = doc.Create.NewGroup(items);
	group.GroupType.Name = IN[1]
except:
	group = list()
TransactionManager.Instance.TransactionTaskDone()

OUT = (group,rejects)