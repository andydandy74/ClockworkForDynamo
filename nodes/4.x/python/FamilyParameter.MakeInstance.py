import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def MakeInstanceParam(doc, param):
	success = False
	if doc.IsFamilyDocument and hasattr(param, "Formula"):
		try:
			doc.FamilyManager.MakeInstance(param)
			success = True
		except: pass
	return param, success

doc = DocumentManager.Instance.CurrentDBDocument
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = map(list, zip(*[MakeInstanceParam(doc, x) for x in IN[0]]))
else: OUT = MakeInstanceParam(doc, IN[0])
TransactionManager.Instance.TransactionTaskDone()