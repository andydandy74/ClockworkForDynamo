import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def DuplicateView(view, name, doc):
	try:
		newViewId = view.Duplicate(Autodesk.Revit.DB.ViewDuplicateOption.Duplicate)
		newView = doc.GetElement(newViewId)
		try: newView.Name = name
		except: pass
		return newView
	except: return None

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	OUT = []
	for view, name in zip(views, IN[1]):
		if isinstance(name, list): OUT.append([DuplicateView(view, x, doc) for x in name])
		else: OUT.append(DuplicateView(view, name, doc))
else: 
	if isinstance(IN[1], list): OUT = [DuplicateView(views, x, doc) for x in IN[1]]
	else: OUT = DuplicateView(views, IN[1], doc)
TransactionManager.Instance.TransactionTaskDone()