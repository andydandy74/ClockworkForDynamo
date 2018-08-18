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
faminsts = UnwrapElement(IN[0])
famsymb = UnwrapElement(IN[1])
booleans = list()
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
for item in faminsts:
	try:
		item.RoomTagType = famsymb[counter]
		booleans.append(True)
	except:
		booleans.append(False)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = (faminsts, booleans)