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

def SetFamilyInstanceLevel(item, lvl):
	try:
		item.get_Parameter(BuiltInParameter.FAMILY_LEVEL_PARAM).Set(lvl.Id)
		return True
	except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetFamilyInstanceLevel(x, y) for x,y in zip(items, lvls)]
	else: OUT = [SetFamilyInstanceLevel(x, lvls) for x in items]
else:
	if isinstance(IN[1], list): OUT = SetFamilyInstanceLevel(items, lvls[0])
	else: OUT = SetFamilyInstanceLevel(items, lvls)
TransactionManager.Instance.TransactionTaskDone()