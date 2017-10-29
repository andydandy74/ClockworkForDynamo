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
texts = IN[1]
booleans = list()
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
while counter < len(items):
	try:
		items[counter].Text = texts[counter]
		booleans.append(True)
	except:
		booleans.append(False)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = (items,booleans)