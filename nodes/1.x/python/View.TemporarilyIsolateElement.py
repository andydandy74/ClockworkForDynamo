import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])
ids = list()
booleans = []
for item in elements:
	ids.append(item.Id)
ielements = List[ElementId](ids)

TransactionManager.Instance.EnsureInTransaction(doc)
try:
	view.IsolateElementsTemporary(ielements)
	booleans.append(True)
except: booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = (view,elements,booleans)