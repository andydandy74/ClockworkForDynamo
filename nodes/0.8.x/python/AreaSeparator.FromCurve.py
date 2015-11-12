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
elementlist = list()

if str(view.ViewType) == "AreaPlan":
	TransactionManager.Instance.EnsureInTransaction(doc)
	doccreation = doc.Create
	for curve in curves:
		separator = doccreation.NewAreaBoundaryLine(sketchplane, curve.ToRevitType(), view)
		elementlist.append(separator)
	TransactionManager.Instance.TransactionTaskDone()
else:
	elementlist = list("The active view needs to be an area plan...")
OUT = elementlist