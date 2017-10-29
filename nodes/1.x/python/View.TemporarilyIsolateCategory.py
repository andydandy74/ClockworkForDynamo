import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
cats = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])
ids = list()

for cat in cats:
	ids.append(cat.Id)
icats = List[ElementId](ids)

TransactionManager.Instance.EnsureInTransaction(doc)
try:
	view.IsolateCategoriesTemporary(icats)
	OUT = (view, True)
except: OUT = (view, False)
TransactionManager.Instance.TransactionTaskDone()