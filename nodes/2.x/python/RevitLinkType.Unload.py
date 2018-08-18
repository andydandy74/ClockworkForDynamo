import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
linktypes = UnwrapElement(IN[0])
unload_locally = IN[1]
booleans = list()

TransactionManager.Instance.ForceCloseTransaction()
for link in linktypes:
	try:
		if unload_locally and doc.IsWorkshared:
			link.UnloadLocally(None)
		else:
			link.Unload(None)
		booleans.append(True)
	except:
		booleans.append(False)
OUT = (linktypes, booleans)