import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def TagIsInRoom(tag):
	if hasattr(tag, "IsInRoom"): return tag.IsInRoom
	else: return False

doc = DocumentManager.Instance.CurrentDBDocument
roomtags = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [TagIsInRoom(x) for x in roomtags]
else: OUT = TagIsInRoom(roomtags)