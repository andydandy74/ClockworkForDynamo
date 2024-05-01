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

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])
phases = UnwrapElement(IN[1])

def SetViewPhase(view, phase):
	try:
		view.get_Parameter(BuiltInParameter.VIEW_PHASE).Set(phase.Id)
		return True
	except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetViewPhase(x, y) for x, y in zip(views, phases)]
	else: OUT = [SetViewPhase(x, phases) for x in views]
else:
	if isinstance(IN[1], list): OUT = SetViewPhase(views, phases[0])
	else: OUT = SetViewPhase(views, phases)
TransactionManager.Instance.TransactionTaskDone()