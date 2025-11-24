import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def DependentToIndependent(view):
	try:
		view.ConvertToIndependent()
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [DependentToIndependent(x) for x in views]
else: OUT = DependentToIndependent(views)
TransactionManager.Instance.TransactionTaskDone()