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

doc = DocumentManager.Instance.CurrentDBDocument
points = IN[0]
phase = UnwrapElement(IN[1])
roomlist = list()
for pt in points:
    roomlist.append(doc.GetRoomAtPoint(pt.ToXyz(),phase))
OUT = roomlist