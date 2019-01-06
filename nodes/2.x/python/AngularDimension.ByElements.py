import clr
from System.Collections.Generic import *

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
opt = Options()
opt.ComputeReferences = True
opt.IncludeNonVisibleObjects = True

items = UnwrapElement(IN[0])
arcs = [x.ToRevitType() for x in IN[1]]
view = UnwrapElement(IN[2])
dimtype = UnwrapElement(IN[3])

def CreateAngularDimension(view, items, arc, dimtype):
	opt.View = view
	refs = []
	for item in items:
		for obj in item.get_Geometry(opt):
			if isinstance (obj, Line):
				curve = obj
				if curve.Reference: refs.append(curve.Reference)
	refList = List[Reference](refs)
	#return refList
	return AngularDimension.Create(doc, view, arc, refList, dimtype)

TransactionManager.Instance.EnsureInTransaction(doc)
OUT = [CreateAngularDimension(view, x, y, dimtype) for x, y in zip(items, arcs)]
TransactionManager.Instance.TransactionTaskDone()

"""
TransactionManager.Instance.EnsureInTransaction(doc)
curvearray = CurveArray()
for curve in curves:
	curvearray.Append(curve.ToRevitType())
doccreation = doc.Create
separatorarray = doccreation.NewRoomBoundaryLines(sketchplane, curvearray, view)
TransactionManager.Instance.TransactionTaskDone()

elementlist = list()
for item in separatorarray:
	elementlist.append(item)
OUT = elementlist
"""