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

TransactionManager.Instance.EnsureInTransaction(doc)
for slab in slabs:
	objtype = slab.GetType().ToString()
	if objtype == "Autodesk.Revit.DB.FootPrintRoof" or objtype == "Autodesk.Revit.DB.Floor":
		try:
			slab.SlabShapeEditor.ResetSlabShape()
			success.append(True)
		except: success.append(False)
	else: success.append(False)
TransactionManager.Instance.TransactionTaskDone()

OUT = (slabs, success)