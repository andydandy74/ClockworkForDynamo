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

def SetText(item, str):
	if hasattr(item, "Text"):
		item.Text = str
		return True
	else: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetText(x, y) for x, y in zip(items, IN[1])]
	else: OUT = [SetText(x, IN[1]) for x in items]
else:
	if isinstance(IN[1], list): OUT = False
	else: OUT = SetText(items, IN[1])
TransactionManager.Instance.TransactionTaskDone()