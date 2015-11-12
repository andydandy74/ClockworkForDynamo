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
successlist = list()
faillist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
slabshape.SlabShapeEditor.ResetSlabShape()
for item in xyzs:
	slabshape.SlabShapeEditor.DrawPoint(item.ToXyz())
TransactionManager.Instance.TransactionTaskDone()

OUT = slabshape