import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
diminsts = UnwrapElement(IN[0])
dimtype = UnwrapElement(IN[1])
booleans = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in diminsts:
	try:
		item.DimensionType = dimtype
		booleans.append(True)
	except:
		booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = (diminsts,booleans)