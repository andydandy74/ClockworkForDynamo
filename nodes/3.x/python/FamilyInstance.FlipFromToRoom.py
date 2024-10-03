import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
faminstances = UnwrapElement(IN[0])
booleans = []

TransactionManager.Instance.EnsureInTransaction(doc)
for item in faminstances:
    try:
        item.FlipFromToRoom()
        booleans.append(True)
    except:
        booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = (faminstances,booleans)