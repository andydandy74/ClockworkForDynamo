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

def RoomByTag(tag):
    room = None
    if hasattr(tag, "TaggedRoomId"):
        trID = tag.TaggedRoomId
        if trID.HostElementId != ElementId.InvalidElementId:
            room = doc.GetElement(trID.HostElementId)
        elif trID.LinkedElementId != ElementId.InvalidElementId:
            linkdoc = doc.GetElement(trID.LinkInstanceId).GetLinkDocument()
            room = linkdoc.GetElement(trID.LinkedElementId)
    return room

doc = DocumentManager.Instance.CurrentDBDocument
roomtags = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [RoomByTag(x) for x in roomtags]
else: OUT = RoomByTag(roomtags)