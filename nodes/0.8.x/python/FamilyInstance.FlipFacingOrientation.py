import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
faminstances = UnwrapElement(IN[0])
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in faminstances:
	try:
		item.flipFacing()
		elementlist.append(item)
	except:
		elementlist.append(list())
TransactionManager.Instance.TransactionTaskDone()
		
OUT = elementlist