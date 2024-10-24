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

points = IN[0]
phase = UnwrapElement(IN[1])
inputdoc = UnwrapElement(IN[2])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

if isinstance(IN[0], list): OUT = [doc.GetRoomAtPoint(x.ToXyz(),phase) for x in points]
else: OUT = doc.GetRoomAtPoint(points.ToXyz(),phase)