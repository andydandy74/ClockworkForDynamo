import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
walls = UnwrapElement(IN[0])

def FlipWall(item):
	if hasattr(item, "Flip"):
		try:
			item.Flip()
			return True
		except: return False
	else: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [FlipWall(x) for x in walls]
else: OUT = FlipWall(walls)
TransactionManager.Instance.TransactionTaskDone()