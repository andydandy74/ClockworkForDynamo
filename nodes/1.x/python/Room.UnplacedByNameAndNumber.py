import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
doccreation = doc.Create
names = IN[0]
numbers = IN[1]
phase = UnwrapElement(IN[2])
counter = 0
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for name in names:
	try:
		newroom = doccreation.NewRoom(phase)
		newroom.Name = name
		newroom.Number = numbers[counter]
		elementlist.append(newroom)
	except: elementlist.append(None)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist