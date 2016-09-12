import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
elementlist = list()
curvelist = list()

for item in items:
	doc = item.Document
	calculator = SpatialElementGeometryCalculator(doc)
	options = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
	# get boundary location from area computation settings
	boundloc = Autodesk.Revit.DB.AreaVolumeSettings.GetAreaVolumeSettings(doc).GetSpatialElementBoundaryLocation(SpatialElementType.Room)
	options.SpatialElementBoundaryLocation = boundloc
	#method #1 - get boundary segments
	blist = list()
	clist = list()
	try:
		for boundarylist in item.GetBoundarySegments(options):
			for boundary in boundarylist:
				blist.append(doc.GetElement(boundary.ElementId))
				clist.append(boundary.Curve.ToProtoType())
	except:
		pass
	#method #2 - spatial element geometry calculator
	try:
		results = calculator.CalculateSpatialElementGeometry(item)
		for face in results.GetGeometry().Faces:
			for bface in results.GetBoundaryFaceInfo(face):
				blist.append(doc.GetElement(bface.SpatialBoundaryElement.HostElementId))
	except:
		pass	
	# write results to list
	elementlist.append(blist)
	curvelist.append(clist)
OUT = (elementlist,curvelist)