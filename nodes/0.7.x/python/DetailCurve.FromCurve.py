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
for curve in curves:
	detcurve = doc.Create.NewDetailCurve(view, curve.ToRevitType())
	elementlist.append(detcurve)
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist