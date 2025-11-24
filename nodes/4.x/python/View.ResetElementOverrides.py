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
view = UnwrapElement(IN[1])
booleans = []

override = OverrideGraphicSettings()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in items:
	try:
		view.SetElementOverrides(item.Id, override)
		booleans.append(True)
	except: booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = (items,view,booleans)