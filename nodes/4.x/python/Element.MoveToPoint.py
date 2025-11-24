import sys
import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
from RevitServices.Transactions import TransactionManager
from RevitServices.Persistence import DocumentManager
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument

elements = UnwrapElement(IN[0])
points = UnwrapElement(IN[1])

def MoveToPoint(item, point):
	try:
		res = item.Location.Move(point.ToXyz(True))
		return (item, res)
	except: return (item, False)
	
TransactionManager.Instance.EnsureInTransaction(doc)
OUT = []
if isinstance(IN[0], list):
	if isinstance(IN[1], list): results = [MoveToPoint(x, y) for x, y in zip(elements, points)]
	else: results = [MoveToPoint(x, points) for x in elements]
	OUT = list(zip(*results))
else:
	if isinstance(IN[1], list): OUT = MoveToPoint(elements, points[0])
	else: OUT = MoveToPoint(elements, points)
TransactionManager.Instance.TransactionTaskDone()