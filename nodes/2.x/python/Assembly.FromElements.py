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
element_array = UnwrapElement(IN[0])
assembly_names = IN[1]
assembly_list = list()

# create assemblies
TransactionManager.Instance.EnsureInTransaction(doc)
for arr in element_array:
	# create a Revit-compatible list of IDs
	ids = list()
	for elem in arr:
		ids.append(elem.Id)	
	idlist = List[ElementId](ids)
	assembly_list.append(AssemblyInstance.Create(doc, idlist, arr[0].Category.Id))
TransactionManager.Instance.TransactionTaskDone()
TransactionManager.Instance.ForceCloseTransaction()
# rename assembly types
i = 0
TransactionManager.Instance.EnsureInTransaction(doc)
for assinst in assembly_list:
	assinst.AssemblyTypeName = assembly_names[i]
	i += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = assembly_list