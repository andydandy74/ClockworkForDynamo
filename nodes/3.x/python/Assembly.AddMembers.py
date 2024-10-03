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
assemblies = UnwrapElement(IN[0])
element_array = UnwrapElement(IN[1])

def AddAssemblyMembers(assembly, items):
	if not hasattr(items, "__iter__"): items = [items]
	ids = [x.Id for x in items]
	idlist = List[ElementId](ids)
	try:
		assembly.AddMemberIds(idlist)
		return assembly
	except: return None

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(assemblies, list): OUT = [AddAssemblyMembers(x,y) for x, y in zip(assemblies, element_array)]
else: OUT = AddAssemblyMembers(assemblies, element_array)
TransactionManager.Instance.TransactionTaskDone()