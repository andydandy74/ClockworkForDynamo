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
items = UnwrapElement(IN[0])
elementlist = list()
curvelist = list()

calculator = SpatialElementGeometryCalculator(doc)
options = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
# get boundary location from area computation settings
boundloc = Autodesk.Revit.DB.AreaVolumeSettings.GetAreaVolumeSettings(doc).GetSpatialElementBoundaryLocation(SpatialElementType.Room)
options.SpatialElementBoundaryLocation = boundloc
for item in items:
	#method #1 - get boundary segments
	blist = list()
	clist = list()
	try:
		for boundarylist in item.GetBoundarySegments(options):
			for boundary in boundarylist:
				blist.append(boundary.Element)
				clist.append(boundary.Curve.ToProtoType())
	except:
		donothing = 1
	#method #2 - spatial element geometry calculator
	try:
		results = calculator.CalculateSpatialElementGeometry(item)
		for face in results.GetGeometry().Faces:
			for bface in results.GetBoundaryFaceInfo(face):
				blist.append(doc.GetElement(bface.SpatialBoundaryElement.HostElementId))
	except:
		donothing = 1	
	# write results to list
	elementlist.append(blist)
	curvelist.append(clist)
OUT = (elementlist,curvelist)