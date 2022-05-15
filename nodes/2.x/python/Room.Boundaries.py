import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

def GetRoomBoundaries(item, version):
	doc = item.Document
	calculator = SpatialElementGeometryCalculator(doc)
	options = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
	# get boundary location from area computation settings
	boundloc = Autodesk.Revit.DB.AreaVolumeSettings.GetAreaVolumeSettings(doc).GetSpatialElementBoundaryLocation(SpatialElementType.Room)
	options.SpatialElementBoundaryLocation = boundloc
	# get boundary segments
	elements = []
	curves = []
	try:
		for boundarylist in item.GetBoundarySegments(options):
			for boundary in boundarylist:
				# fix possibly missing bounding element in previous entry
				if len(elements) > 2:
					if elements[-1] == None:
						if boundary.ElementId == elements[-2].Id: 
							elements[-1] = doc.GetElement(boundary.ElementId)
				# add boundary to list
				elements.append(doc.GetElement(boundary.ElementId))
				if version > 2016: curves.append(boundary.GetCurve().ToProtoType())
				else: curves.append(boundary.Curve.ToProtoType())
	except: pass
	return elements, curves

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetRoomBoundaries(x, IN[1]) for x in items]))
else: OUT = GetRoomBoundaries(items, IN[1])