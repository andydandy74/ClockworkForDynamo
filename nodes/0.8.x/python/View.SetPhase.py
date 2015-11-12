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
phase = UnwrapElement(IN[1])
booleans = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for view in views:
	try:
		view.get_Parameter(BuiltInParameter.VIEW_PHASE).Set(phase.Id)
		booleans.append(True)
	except:
		booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = (views,booleans)