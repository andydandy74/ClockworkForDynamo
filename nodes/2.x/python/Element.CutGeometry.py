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

def CutGeometry(doc, item1, item2):
	try:
		SolidSolidCutUtils.AddCutBetweenSolids(doc,item1,item2)
		return True
	except:
		try:
			InstanceVoidCutUtils.AddInstanceVoidCut(doc,item1,item2)
			return True
		except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [CutGeometry(doc, x, y) for x, y in zip(items1, items2)]
	else: OUT = [CutGeometry(doc, x, items2) for x in items1]
else:
	if isinstance(IN[1], list): OUT = [CutGeometry(doc, items1, x) for x in items2]
	else: OUT = CutGeometry(doc, items1, items2)
TransactionManager.Instance.TransactionTaskDone()