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
names = IN[1]

def MakeAssembly(items):
	try: 
		idlist = List[ElementId]([x.Id for x in items])
		return AssemblyInstance.Create(doc, idlist, items[0].Category.Id)
	except: return None

# create assemblies
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(names, list): OUT = [MakeAssembly(x) for x in element_array]
else: OUT = MakeAssembly(element_array)
TransactionManager.Instance.TransactionTaskDone()
TransactionManager.Instance.ForceCloseTransaction()
# rename assembly types after assemblies have been committed
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(names, list): 
	for x,y in zip(OUT, names):
		if x:
			try: x.AssemblyTypeName = y
			except: pass
elif OUT: 
	try: OUT.AssemblyTypeName = names
	except: pass
TransactionManager.Instance.TransactionTaskDone()