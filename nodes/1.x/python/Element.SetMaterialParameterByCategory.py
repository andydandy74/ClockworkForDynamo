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
elementlist = list()
failedlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in elements:
	try:
		paramset = False
		for param in item.Parameters:
			if param.Definition.Name == paramname:
				param.Set(ElementId.InvalidElementId)
				elementlist.append(item)
				paramset = True
		if paramset == False:
			failedlist.append(item)
	except:
		failedlist.append(item)
TransactionManager.Instance.TransactionTaskDone()

OUT = (elementlist,failedlist)