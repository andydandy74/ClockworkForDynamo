import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items1 = UnwrapElement(IN[0])
items2 = UnwrapElement(IN[1])
i = 0
booleans = list()
TransactionManager.Instance.EnsureInTransaction(doc)
for item1 in items1:
	try:
		SolidSolidCutUtils.AddCutBetweenSolids(doc,item1,items2[i])
		booleans.append(True)
	except:
		try:
			InstanceVoidCutUtils.AddInstanceVoidCut(doc,item1,items2[i])
			booleans.append(True)
		except:
			booleans.append(False)
	i += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = booleans