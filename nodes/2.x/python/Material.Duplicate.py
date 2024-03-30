import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def DuplicateMaterial(mat, name):
	try: return mat.Duplicate(name)
	except: return None

doc = DocumentManager.Instance.CurrentDBDocument
mats = UnwrapElement(IN[0])
newnames = IN[1]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(mats, list): OUT = [DuplicateMaterial(x, y) for x, y in zip(mats, newnames)]
else: OUT = DuplicateMaterial(mats, newnames)
TransactionManager.Instance.TransactionTaskDone()