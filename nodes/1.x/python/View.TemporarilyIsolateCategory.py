import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def TempIsolateCategories(view, cats):
	if not cats: return False
	elif not isinstance(cats, list): cats = [cats]
	icats = List[ElementId]([x.Id for x in cats])
	try:
		UnwrapElement(view).IsolateCategoriesTemporary(icats)
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[1], list):
	if isinstance(IN[0], list): OUT = [TempIsolateCategories(x, y) for x, y in zip(IN[1], IN[0])]
	else: OUT = [TempIsolateCategories(x, IN[0]) for x in IN[1]]
else: OUT = TempIsolateCategories(IN[1], IN[0])
TransactionManager.Instance.TransactionTaskDone()