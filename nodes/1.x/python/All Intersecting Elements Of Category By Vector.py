import clr
from System.Collections.Generic import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])

def DeleteElement(item):
	if hasattr(item, "Id"):
		try: 
			doc.Delete(item.Id)
			return True
		except: return False
	else: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [DeleteElement(x) for x in items]
else: OUT = DeleteElement(items)
TransactionManager.Instance.TransactionTaskDone()