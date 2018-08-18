import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
fams = UnwrapElement(IN[0])
cutters = UnwrapElement(IN[1])
booleans = []
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
for fam in fams:
	try:
		fam.RemoveCoping(cutters[counter])
		booleans.append(True)
	except:	booleans.append(False)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = (fams,booleans)