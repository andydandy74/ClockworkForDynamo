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

doc = DocumentManager.Instance.CurrentDBDocument
xyzs = IN[0]
slabshape = UnwrapElement(IN[1])
booleans = []

TransactionManager.Instance.EnsureInTransaction(doc)
for item in xyzs:
	try:
		slabshape.SlabShapeEditor.DrawPoint(item.ToXyz())
		booleans.append(True)
	except: booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = (slabshape,booleans)