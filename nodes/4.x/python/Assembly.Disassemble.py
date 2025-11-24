import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def ExplodeAssembly(assembly):
	if hasattr(assembly, "Disassemble"): return [doc.GetElement(x) for x in assembly.Disassemble()]
	else: return list()

doc = DocumentManager.Instance.CurrentDBDocument
assemblies = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [ExplodeAssembly(x) for x in assemblies]
else: OUT = ExplodeAssembly(assemblies)
TransactionManager.Instance.TransactionTaskDone()