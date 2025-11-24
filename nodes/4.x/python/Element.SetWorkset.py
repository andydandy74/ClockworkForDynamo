import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
worksets = UnwrapElement(IN[1])

def SetWorkset(item, ws):
	if hasattr(ws, "Id"):
		# Is this an archi-lab workset?
		if isinstance(ws.Id, int): wsID = ws.Id
		else: wsID = ws.Id.IntegerValue
		try:
			item.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(wsID)
			return True
		except: return False
	else: return False
	
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetWorkset(x, y) for x, y in zip(items, worksets)]
	else: OUT = [SetWorkset(x, worksets) for x in items]
else:
	if isinstance(IN[1], list): OUT = SetWorkset(items, worksets[0])
	else: OUT = SetWorkset(items, worksets)
TransactionManager.Instance.TransactionTaskDone()