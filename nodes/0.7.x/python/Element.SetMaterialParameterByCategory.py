import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])
param = IN[1]
elementlist = list()
failedlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in elements:
	try:
		item.Parameter[param].Set(ElementId(-1))
		elementlist.append(item)
	except:
		failedlist.append(item)
TransactionManager.Instance.TransactionTaskDone()

OUT = (elementlist,failedlist)