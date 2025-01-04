import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
faminstances = UnwrapElement(IN[0])

def FlipRoom(item):
	try:
		item.FlipFromToRoom()
		return True
	except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [FlipRoom(x) for x in faminstances]
else: OUT = FlipRoom(faminstances)
TransactionManager.Instance.TransactionTaskDone()