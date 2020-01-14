import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
version = IN[1]

def GetDependentOld(item):
	# We will need a transaction in order to 
	# temporarily delete the elements and see what dependes on them.
	# Although the new method already exists in 2018.1
	# it requires an element filter up to 2019.0 which to me doesn't make a whole lot of sense
	# (which is probably why they changed that for 2019...).
	TransactionManager.Instance.EnsureInTransaction(doc)
	trans = SubTransaction(doc)
	trans.Start()
	try: dependents = doc.Delete(item.Id)
	except: dependents = []
	trans.RollBack()
	TransactionManager.Instance.TransactionTaskDone()
	return [doc.GetElement(x) for x in dependents if x != item.Id]

def GetDependentNew(item):
	if hasattr(item, "GetDependentElements"): 
		return [doc.GetElement(x) for x in item.GetDependentElements(None) if x != item.Id]
	else: return []
	
if version < 2019:	
	if isinstance(IN[0], list): OUT = [GetDependentOld(x) for x in items]
	else: OUT = GetDependentOld(items)	
else:
	if isinstance(IN[0], list): OUT = [GetDependentNew(x) for x in items]
	else: OUT = GetDependentNew(items)