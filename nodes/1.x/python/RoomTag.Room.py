import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

roomtags = UnwrapElement(IN[0])
elementlist = list()

for tag in roomtags:
	try:
		elementlist.append(tag.Room)
	except:
		elementlist.append(list())
OUT = elementlist