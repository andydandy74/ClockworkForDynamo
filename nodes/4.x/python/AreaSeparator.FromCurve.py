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
elementlist = []

TransactionManager.Instance.EnsureInTransaction(doc)
o = view.Origin
n = view.ViewDirection
if o and n: 
	sketchplane = SketchPlane.Create(doc, Plane.CreateByNormalAndOrigin(n, o))
	doccreation = doc.Create
	for curve in curves:
		separator = doccreation.NewAreaBoundaryLine(sketchplane, curve.ToRevitType(), view)
		elementlist.append(separator)
TransactionManager.Instance.TransactionTaskDone()

if isinstance(IN[0], list): OUT = elementlist
else: OUT = elementlist[0]