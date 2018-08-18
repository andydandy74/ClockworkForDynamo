import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def CreateUnplacedRoom(name, number, phase, doc):
	try:
		newroom = doc.Create.NewRoom(phase)
		newroom.Name = name
		newroom.Number = number
		return newroom
	except: return None

doc = DocumentManager.Instance.CurrentDBDocument
phase = UnwrapElement(IN[2])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list) and isinstance(IN[1], list): OUT = [CreateUnplacedRoom(x, y, phase, doc) for x, y in zip(IN[0], IN[1])]
else: OUT = None
TransactionManager.Instance.TransactionTaskDone()