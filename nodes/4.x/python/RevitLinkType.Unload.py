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

def UnloadLinkType(linktype):
	try:
		if unload_locally and doc.IsWorkshared: linktype.UnloadLocally(None)
		else: linktype.Unload(None)
		return True
	except: return False

TransactionManager.Instance.ForceCloseTransaction()
if isinstance(IN[0], list): OUT = [UnloadLinkType(x) for x in linktypes]
else: OUT = UnloadLinkType(linktypes)