import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
points = UnwrapElement(IN[0])
famtypes = UnwrapElement(IN[1])
views = UnwrapElement(IN[2])

def FamInstViewBased(point, ft, view):
	# make sure familysymbol is active
	if ft.IsActive == False:
		ft.Activate()
		doc.Regenerate()
	newobj = doc.Create.NewFamilyInstance(point.ToXyz(),ft,view)
	return newobj.ToDSType(False)

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list):
		if isinstance(IN[2], list): OUT = [FamInstViewBased(x, y, z) for x, y, z in zip(points, famtypes, views)]
		else: OUT = [FamInstViewBased(x, y, views) for x, y in zip(points, famtypes)]
	else:
		if isinstance(IN[2], list): OUT = [FamInstViewBased(x, famtypes, y) for x, y in zip(points, views)]
		else: OUT = [FamInstViewBased(x, famtypes, views) for x in points]
else:
	if isinstance(IN[1], list):
		if isinstance(IN[2], list): OUT = FamInstViewBased(points, famtypes[0], views[0])
		else: OUT = FamInstViewBased(points, famtypes[0], views)
	else:
		if isinstance(IN[2], list): OUT = FamInstViewBased(points, famtypes, views[0])
		else: OUT = FamInstViewBased(points, famtypes, views)
TransactionManager.Instance.TransactionTaskDone()