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
famtypes = UnwrapElement(IN[0])
newnames = IN[1]
elementlist = list()
counter = 0
TransactionManager.Instance.EnsureInTransaction(doc)
for item in famtypes:
	try:
		elementlist.append(item.Duplicate(newnames[counter]))
	except:
		elementlist.append(list())
	counter += 1
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist