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
elements = UnwrapElement(IN[1])

def RemoveAssemblyMembers(assembly, members):
	if isinstance(members, list): items = members
	else: items = [members]
	# create a Revit-compatible list of IDs
	ids = list()
	[ids.append(x.Id) for x in items]	
	idlist = List[ElementId](ids)
	try:
		assembly.RemoveMemberIds(idlist)
		return assembly, True
	except: return assembly, False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): results = [RemoveAssemblyMembers(x, y) for x,y in zip(assemblies, elements)]
	else: results = [RemoveAssemblyMembers(x, elements) for x in assemblies]
	OUT = list(zip(*results))
else: OUT = RemoveAssemblyMembers(assemblies, elements)
TransactionManager.Instance.TransactionTaskDone()