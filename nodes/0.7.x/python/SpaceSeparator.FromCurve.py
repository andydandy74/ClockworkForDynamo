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
sketchplane = UnwrapElement(IN[1])
view = UnwrapElement(IN[2])

TransactionManager.Instance.EnsureInTransaction(doc)
curvearray = CurveArray()
for curve in curves:
	curvearray.Append(curve.ToRevitType())
doccreation = doc.Create
separatorarray = doccreation.NewSpaceBoundaryLines(sketchplane, curvearray, view)
TransactionManager.Instance.TransactionTaskDone()

elementlist = list()
for item in separatorarray:
	elementlist.append(item)
OUT = elementlist