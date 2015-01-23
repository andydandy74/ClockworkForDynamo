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
names = IN[1]
goodlist = list()
badlist = list()
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
while counter &lt; len(items):
	try:
		items[counter].Name = names[counter]
		goodlist.append(items[counter].ToDSType(True))
	except:
		badlist.append(items[counter].ToDSType(True))
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = (goodlist,badlist)