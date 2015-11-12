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
booleans = list()
counter = 0
TransactionManager.Instance.EnsureInTransaction(doc)
for item in views:
	try:
		p = item.get_Parameter(BuiltInParameter.VIEWER_OPTION_VISIBILITY)
		p.Set(options[counter].Id)
		booleans.append(True)
	except:
		booleans.append(False)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()
OUT = (views,booleans)