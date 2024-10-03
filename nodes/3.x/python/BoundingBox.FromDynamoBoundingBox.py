import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def MakeBoundingBox(min, max):
	try:
		newbox = BoundingBoxXYZ()
		newbox.Max = max.ToXyz()
		newbox.Min = min.ToXyz()
		return newbox
	except: return None

doc = DocumentManager.Instance.CurrentDBDocument
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [MakeBoundingBox(x, y) for x, y in zip(IN[0], IN[1])]
else: OUT = MakeBoundingBox(IN[0], IN[1])
TransactionManager.Instance.TransactionTaskDone()