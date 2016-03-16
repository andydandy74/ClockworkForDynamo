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
assembly = UnwrapElement(IN[0])
element_array = UnwrapElement(IN[1])

# add items to assembly
TransactionManager.Instance.EnsureInTransaction(doc)
# create a Revit-compatible list of IDs
ids = list()
for elem in element_array:
	ids.append(elem.Id)	
idlist = List[ElementId](ids)
try:
	assembly.AddMemberIds(idlist)
	OUT = assembly
except:
	OUT = None
TransactionManager.Instance.TransactionTaskDone()