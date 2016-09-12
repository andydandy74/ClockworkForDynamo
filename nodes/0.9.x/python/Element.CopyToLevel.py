import clr
from System.Collections.Generic import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
source_view = UnwrapElement(IN[1])
target_view = UnwrapElement(IN[2])

ids = list()
for item in items:
	ids.append(item.Id)	
itemlist = List[ElementId](ids)

TransactionManager.Instance.EnsureInTransaction(doc)
newitems = ElementTransformUtils.CopyElements(source_view,itemlist,target_view, None, None)
TransactionManager.Instance.TransactionTaskDone()

elementlist = list()
for item in newitems:
	elementlist.append(doc.GetElement(item).ToDSType(False))

OUT = elementlist