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
railingtype = UnwrapElement(IN[1])
lvl = UnwrapElement(IN[2])

TransactionManager.Instance.EnsureInTransaction(doc)
curveloop = CurveLoop.Create([x.ToRevitType() for x in curves])
OUT = Architecture.Railing.Create(doc, curveloop, railingtype.Id, lvl.Id)
TransactionManager.Instance.TransactionTaskDone()