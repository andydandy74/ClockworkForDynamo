import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
linkpaths = IN[0]
elementlist = list()
booleans = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for path in linkpaths:
	try:
		linkpath = ModelPathUtils.ConvertUserVisiblePathToModelPath(path)
		linkoptions = RevitLinkOptions(False)
		linkloadresult = RevitLinkType.Create(doc, linkpath, linkoptions)
		elementlist.append(RevitLinkInstance.Create(doc, linkloadresult.ElementId))
		booleans.append(True)
	except:
		booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = (elementlist, booleans)