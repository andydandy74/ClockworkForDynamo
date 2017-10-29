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
detailLevel = UnwrapElement(IN[1])
if IN[1] == "Coarse": dl = 1
elif IN[1] == "Medium": dl = 2
elif IN[1] == "Fine": dl = 3
else: dl = 0
booleans = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for view in views:
	try:
		view.get_Parameter(BuiltInParameter.VIEW_DETAIL_LEVEL).Set(dl)
		booleans.append(True)
	except:
		booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = (views,booleans)