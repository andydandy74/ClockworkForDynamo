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
cats = UnwrapElement(IN[0])

def ResetCatMat(cat):
	if hasattr(cat, "Material"): 
		cat.Material = doc.GetElement(ElementId.InvalidElementId)
		return True
	else: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [ResetCatMat(x) for x in cats]
else: OUT = ResetCatMat(cats)
TransactionManager.Instance.TransactionTaskDone()