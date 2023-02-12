import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

views = UnwrapElement(IN[0])
bboxes = IN[1]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [x.SetSectionBox(y) for x, y in zip(views, bboxes)]
	else: OUT = [x.SetSectionBox(bboxes) for x in views]
else:
	if isinstance(IN[1], list): OUT = views.SetSectionBox(bboxes[0])
	else: OUT = views.SetSectionBox(bboxes)
TransactionManager.Instance.TransactionTaskDone()

OUT = views