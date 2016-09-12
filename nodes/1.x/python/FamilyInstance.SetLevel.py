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
items = UnwrapElement(IN[0])
lvls = UnwrapElement(IN[1])
booleans = list()
i = 0

TransactionManager.Instance.EnsureInTransaction(doc)
for item in items:
	try:
		item.get_Parameter(BuiltInParameter.FAMILY_LEVEL_PARAM).Set(lvls[i].Id)
		booleans.append(True)
	except:
		booleans.append(False)
	i += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = (items,booleans)