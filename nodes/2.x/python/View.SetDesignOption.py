import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])
options = UnwrapElement(IN[1])

def SetViewDesignOption(view, option):
	try:
		view.get_Parameter(BuiltInParameter.VIEWER_OPTION_VISIBILITY).Set(option.Id)
		return True
	except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetViewDesignOption(x, y) for x, y in zip(views, options)]
	else: OUT = [SetViewDesignOption(x, options) for x in views]
else:
	if isinstance(IN[1], list): OUT = [SetViewDesignOption(views, x) for x in options]
	else: OUT = SetViewDesignOption(views, options)
TransactionManager.Instance.TransactionTaskDone()