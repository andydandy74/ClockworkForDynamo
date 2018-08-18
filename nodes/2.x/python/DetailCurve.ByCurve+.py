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
if doc.IsFamilyDocument: 
	doc_create = doc.FamilyCreate
else: 
	doc_create = doc.Create
for curve in curves:
	try:
		detcurve = doc_create.NewDetailCurve(view, curve.ToRevitType())
		elementlist.append(detcurve)
	except:
		elementlist.append(None)
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist