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
if doc.IsFamilyDocument: doc_create = doc.FamilyCreate
else: doc_create = doc.Create
curves = UnwrapElement(IN[0])
views = UnwrapElement(IN[1])

def MakeDetailCurve(curve, view):
	try: return doc_create.NewDetailCurve(view, curve.ToRevitType())
	except: return None

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [MakeDetailCurve(x, y) for x, y in zip(curves, views)]
	else: OUT = [MakeDetailCurve(x, views) for x in curves]
else:
	if isinstance(IN[1], list): OUT = [MakeDetailCurve(curves, x) for x in views]
	else: OUT = MakeDetailCurve(curves, views)
TransactionManager.Instance.TransactionTaskDone()