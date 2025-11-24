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
views = UnwrapElement(IN[0])
margins = IN[1]

def ResizeCropbox(view, marginD):
	try:
		margin = marginD.ToXyz()
		newbox = BoundingBoxXYZ()
		newbox.Max = view.CropBox.Max.Add(margin)
		newbox.Min = view.CropBox.Min.Subtract(margin)
		view.CropBox = newbox
		return True
	except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [ResizeCropbox(x, y) for x, y in zip(views, margins)]
	else: OUT = [ResizeCropbox(x, margins) for x in views]
else:
	if isinstance(IN[0], list): OUT = ResizeCropbox(views, margins[0])
	else: OUT = ResizeCropbox(views, margins)
TransactionManager.Instance.TransactionTaskDone()