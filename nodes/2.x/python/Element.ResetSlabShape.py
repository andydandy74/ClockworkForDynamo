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
slabs = UnwrapElement(IN[0])
success = []

def SlabShapeReset(slab):
	sle = None
	if hasattr(slab, "SlabShapeEditor"): sle = slab.SlabShapeEditor
	elif hasattr(slab, "GetSlabShapeEditor"): sle = slab.GetSlabShapeEditor()
	if sle:
		try:
			sle.ResetSlabShape()
			return slab, True
		except: return slab, False
	else: return slab, False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): 
	results = [SlabShapeReset(x) for x in slabs]
	OUT = list(zip(*results))
else: OUT = SlabShapeReset(slabs)
TransactionManager.Instance.TransactionTaskDone()