import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def SetFormula(param, formula):
	success = False
	if doc.IsFamilyDocument and hasattr(param, "Formula"):
		try:
			doc.FamilyManager.SetFormula(param, formula)
			success = True
		except: pass
	return param, success

doc = DocumentManager.Instance.CurrentDBDocument
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): 
	OUT = map(list, zip(*[SetFormula(x, y) for x, y in zip(IN[0], IN[1])]))
else: OUT = SetFormula(IN[0], IN[1])
TransactionManager.Instance.TransactionTaskDone()