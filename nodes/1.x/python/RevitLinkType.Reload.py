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
booleans = list()

TransactionManager.Instance.ForceCloseTransaction()
for link in linktypes:
	if link.LocallyUnloaded:
		link.RevertLocalUnloadStatus()
	else:
		link.Reload()
	try:
		
		booleans.append(True)
	except:
		booleans.append(False)
OUT = (linktypes, booleans)