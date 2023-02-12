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
mats = UnwrapElement(IN[1])

def SetCatMat(cat, mat):
	if hasattr(cat, "Material"): 
		cat.Material = mat
		return True
	else: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetCatMat(x, y) for x, y in zip(cats, mats)]
	else: OUT = [SetCatMat(x, mats) for x in cats]
else:
	if isinstance(mats, list): OUT = SetCatMat(cats, mats[0])
	else: OUT = SetCatMat(cats, mats)
TransactionManager.Instance.TransactionTaskDone()