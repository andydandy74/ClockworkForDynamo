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

def AddLink(path):
	try:
		linkpath = ModelPathUtils.ConvertUserVisiblePathToModelPath(path)
		linkoptions = RevitLinkOptions(relative)
		linkloadresult = RevitLinkType.Create(doc, linkpath, linkoptions)
		return RevitLinkInstance.Create(doc, linkloadresult.ElementId).ToDSType(False)
	except: return None

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(linkpaths, list): OUT = [AddLink(x) for x in linkpaths]
else: OUT = AddLink(linkpaths)
TransactionManager.Instance.TransactionTaskDone()