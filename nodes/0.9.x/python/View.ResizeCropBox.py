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
margin = IN[1].ToXyz()
elementlist = list()
failedlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for item in views:
	try:
		newmax = item.CropBox.Max.Add(margin)
		newmin = item.CropBox.Min.Subtract(margin)
		newbox = BoundingBoxXYZ()
		newbox.Max = newmax
		newbox.Min = newmin
		item.CropBox = newbox
		elementlist.append(item)
	except:
		elementlist.append(list())
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist