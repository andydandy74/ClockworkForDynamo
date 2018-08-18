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

def AddPointToSlabShape(item, point):
	if hasattr(item, "SlabShapeEditor") and hasattr(point, "ToXyz"):
		try:
			item.SlabShapeEditor.DrawPoint(point.ToXyz())
			return True
		except: return False
	else: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[1])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[1], list):
	if isinstance(IN[0], list):
		OUT = []
		for item, points in zip(items, IN[0]):
			if isinstance(points, list): OUT.append((item, [AddPointToSlabShape(item, x) for x in points]))
			else: OUT.append((item, AddPointToSlabShape(item, points)))
	else: OUT = [(x, AddPointToSlabShape(x, IN[0])) for x in items]
	OUT = map(list, zip(*OUT))
else:
	if isinstance(IN[0], list): OUT = items, [AddPointToSlabShape(items, x) for x in IN[0]]
	else: OUT = items, AddPointToSlabShape(items, IN[0])
TransactionManager.Instance.TransactionTaskDone()