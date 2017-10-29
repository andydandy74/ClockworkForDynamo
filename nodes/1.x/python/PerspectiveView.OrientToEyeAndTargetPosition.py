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
view = UnwrapElement(IN[0])
eyeposition = IN[1].ToXyz()
updirection = IN[2].ToXyz()
forwarddirection = IN[3].ToXyz()

TransactionManager.Instance.EnsureInTransaction(doc)
try:
	newVO = ViewOrientation3D(eyeposition, updirection, forwarddirection)
	view.SetOrientation(newVO)
	view.SaveOrientation()
	OUT = True
except:
	OUT = False
TransactionManager.Instance.TransactionTaskDone()