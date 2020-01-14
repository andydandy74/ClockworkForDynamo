import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
params = UnwrapElement(IN[0])

def AllowVaryBetweenGroups(param, bool):
	if hasattr(param, "GetDefinition"):
		intdef = param.GetDefinition()
		if hasattr(intdef, "SetAllowVaryBetweenGroups"):
			try: 
				intdef.SetAllowVaryBetweenGroups(doc, bool)
				return True
			except: return False
		else: return False
	else: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [AllowVaryBetweenGroups(x, IN[1]) for x in params]
else: OUT = AllowVaryBetweenGroups(params, IN[1])
TransactionManager.Instance.TransactionTaskDone()