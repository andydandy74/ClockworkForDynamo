import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = UnwrapElement(IN[0])
frame = IN[1]
TransactionManager.Instance.EnsureInTransaction(doc)
try:
	view.SunAndShadowSettings.ActiveFrame = frame
	success = True
except:
	success = False
TransactionManager.Instance.TransactionTaskDone()
OUT = (view,success)