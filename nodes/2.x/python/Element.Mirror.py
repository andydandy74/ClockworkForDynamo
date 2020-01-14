import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def MirrorMirror(doc, items, plane, copymode):
	itemids = List[ElementId]([x.Id for x in items])
	mirroredids = ElementTransformUtils.MirrorElements(doc, itemids, plane, copymode)
	if copymode: return [doc.GetElement(x).ToDSType(False) for x in mirroredids]
	else: return items

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
copymode = IN[1]
planenormal = IN[2].ToRevitType()
planeorigin = IN[3].ToRevitType()

TransactionManager.Instance.EnsureInTransaction(doc)
plane = Plane.CreateByNormalAndOrigin(planenormal, planeorigin)
if isinstance(IN[0], list): OUT = MirrorMirror(doc, items, plane, copymode)
else: OUT = MirrorMirror(doc, [items], plane, copymode)[0]
TransactionManager.Instance.TransactionTaskDone()