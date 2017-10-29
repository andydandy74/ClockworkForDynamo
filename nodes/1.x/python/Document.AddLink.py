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
linkpaths = IN[0]
relative = IN[1]
elementlist = list()
booleans = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for path in linkpaths:
	try:
		linkpath = ModelPathUtils.ConvertUserVisiblePathToModelPath(path)
		linkoptions = RevitLinkOptions(relative)
		linkloadresult = RevitLinkType.Create(doc, linkpath, linkoptions)
		elementlist.append(RevitLinkInstance.Create(doc, linkloadresult.ElementId).ToDSType(False))
		booleans.append(True)
	except:
		booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = (elementlist, booleans)