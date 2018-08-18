import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])
paramname = IN[1]
booleans = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in elements:
	try:
		paramset = False
		for param in item.Parameters:
			if param.Definition.Name == paramname:
				param.Set(ElementId.InvalidElementId)
				booleans.append(True)
				paramset = True
				break
		if paramset == False:
			booleans.append(False)
	except:
		booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = (elements,booleans)