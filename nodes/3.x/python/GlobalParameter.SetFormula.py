import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def SetGPFormula(gp,formula):
	try: 
		gp.SetFormula(formula)
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
formulas = IN[1]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): 
	if isinstance(IN[1], list): OUT = [SetGPFormula(x,y) for x,y in zip(items,formulas)]
	else: OUT = [SetGPFormula(x,formulas) for x in items]
else:
	if isinstance(IN[1], list): OUT = SetGPFormula(items,formulas[0])
	else: OUT = SetGPFormula(items,formulas)
TransactionManager.Instance.TransactionTaskDone()