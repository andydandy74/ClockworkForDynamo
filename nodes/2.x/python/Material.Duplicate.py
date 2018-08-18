import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
mats = UnwrapElement(IN[0])
newnames = IN[1]
elementlist, fail = [],[] #better to generate a fail list only once

TransactionManager.Instance.EnsureInTransaction(doc)
for i in xrange(len(mats)):
	try: elementlist.append(mats[i].Duplicate(newnames[i]))
	except: elementlist.append(None)
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist