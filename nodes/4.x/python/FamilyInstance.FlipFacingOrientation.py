import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def FlipFacing(item):
	try:
		item.flipFacing()
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [FlipFacing(x) for x in items]
else: OUT = FlipFacing(items)
TransactionManager.Instance.TransactionTaskDone()