import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def SetDetailLevel(view, level):
	if level == "Coarse": dl = 1
	elif level == "Medium": dl = 2
	elif level == "Fine": dl = 3
	else: return False
	try:
		view.get_Parameter(BuiltInParameter.VIEW_DETAIL_LEVEL).Set(dl)
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetDetailLevel(x, y) for x, y in zip(views, IN[1])]
	else: OUT = [SetDetailLevel(x, IN[1]) for x in views]
else: OUT = SetDetailLevel(views, IN[1])
TransactionManager.Instance.TransactionTaskDone()