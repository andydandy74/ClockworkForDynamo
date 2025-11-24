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
curves = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])


TransactionManager.Instance.EnsureInTransaction(doc)
o = view.Origin
n = view.ViewDirection
if o and n: 
	sketchplane = SketchPlane.Create(doc, Plane.CreateByNormalAndOrigin(n, o))
	curvearray = CurveArray()
	for curve in curves:
		curvearray.Append(curve.ToRevitType())
	doccreation = doc.Create
	separatorarray = doccreation.NewSpaceBoundaryLines(sketchplane, curvearray, view)
else: separatorarray = []
TransactionManager.Instance.TransactionTaskDone()

elementlist = list()
for item in separatorarray:
	elementlist.append(item)
if isinstance(IN[0], list): OUT = elementlist
else: OUT = elementlist[0]