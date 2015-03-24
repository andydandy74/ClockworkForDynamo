import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

rooms = UnwrapElement(IN[0])
points = [x.ToXyz() for x in IN[1]]
roomlist = list()
for room in rooms:
	booleans = list()
	for point in points:
		try:
			if room.IsPointInRoom(point):
				booleans.append(True)
			else:
				booleans.append(False)
		except:
			booleans.append(False)
	roomlist.append(booleans)
OUT = roomlist