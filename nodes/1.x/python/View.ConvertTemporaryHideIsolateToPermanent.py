import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = UnwrapElement(IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)
view.ConvertTemporaryHideIsolateToPermanent()
TransactionManager.Instance.TransactionTaskDone()
OUT = view