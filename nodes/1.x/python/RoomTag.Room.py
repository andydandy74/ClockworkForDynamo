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

doc = DocumentManager.Instance.CurrentDBDocument

roomtags = UnwrapElement(IN[0])
version = IN[1]
elementlist = list()

for tag in roomtags:
	if version > 2016:
		try:
			trID = tag.TaggedRoomId
			if trID.HostElementId.IntegerValue != -1:
				elementlist.append(doc.GetElement(trID.HostElementId))
			elif trID.LinkedElementId.IntegerValue != -1:
				linkdoc = doc.GetElement(trID.LinkInstanceId).GetLinkDocument()
				elementlist.append(linkdoc.GetElement(trID.LinkedElementId))
			else:
				elementlist.append(None)
		except:
			elementlist.append(None)
	else:
		try:
			elementlist.append(tag.Room)
		except:
			elementlist.append(None)
OUT = elementlist