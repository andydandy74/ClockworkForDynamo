import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
params = IN[1]

def ResetMaterialParameter(item, param):
	try:
		paramset = False
		for p in item.Parameters:
			if p.Definition.Name == param:
				p.Set(ElementId.InvalidElementId)
				return True
		return False
	except: return False
		
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [ResetMaterialParameter(x, y) for x, y in zip(items, params)]
	else: OUT = [ResetMaterialParameter(x, params) for x in items]
else:
	if isinstance(IN[1], list): OUT = [ResetMaterialParameter(items, x) for x in params]
	else: OUT = ResetMaterialParameter(items, params)
TransactionManager.Instance.TransactionTaskDone()