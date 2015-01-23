import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
faminsts = UnwrapElement(IN[0])
ws = UnwrapElement(IN[1])
elementlist = list()
faillist = list()
TransactionManager.Instance.EnsureInTransaction(doc)
for item in faminsts:
	try:
		param = item.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM)
		param.Set(ws.Id.IntegerValue)
		elementlist.append(item)
	except:
		faillist.append(item)
TransactionManager.Instance.TransactionTaskDone()
OUT = (elementlist,faillist)