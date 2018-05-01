import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def TempIsolateElements(view, items):
	if not items: return False
	elif not isinstance(items, list): items = [items]
	ielements = List[ElementId]([x.Id for x in UnwrapElement(items)])
	try:
		UnwrapElement(view).IsolateElementsTemporary(ielements)
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[1], list):
	if isinstance(IN[0], list): OUT = [TempIsolateElements(x, y) for x, y in zip(IN[1], IN[0])]
	else: OUT = [TempIsolateElements(x, IN[0]) for x in IN[1]]
else: OUT = TempIsolateElements(IN[1], IN[0])
TransactionManager.Instance.TransactionTaskDone()