import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
facetypes = []
facemats = []
faceelements = []
faceareas = []
faces = []

for item in items:
	doc = item.Document
	calculator = SpatialElementGeometryCalculator(doc)
	options = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
	# get boundary location from area computation settings
	boundloc = Autodesk.Revit.DB.AreaVolumeSettings.GetAreaVolumeSettings(doc).GetSpatialElementBoundaryLocation(SpatialElementType.Room)
	options.SpatialElementBoundaryLocation = boundloc
	mlist = []
	tlist = []
	elist = []
	alist = []
	flist = []
	try:
		results = calculator.CalculateSpatialElementGeometry(item)
		for face in results.GetGeometry().Faces:
			for bface in results.GetBoundaryFaceInfo(face):
				tlist.append(str(bface.SubfaceType))
				eId = bface.SpatialBoundaryElement.HostElementId
				if eId == ElementId.InvalidElementId:
					liId = bface.SpatialBoundaryElement.LinkInstanceId
					if liId == ElementId.InvalidElementId: 
						elist.append(None)
						mlist.append(None)
					else:
						leId = bface.SpatialBoundaryElement.LinkedElementId
						if leId == ElementId.InvalidElementId: 
							elist.append(None)
							mlist.append(None)
						else: 
							elist.append(doc.GetElement(liId).GetLinkDocument().GetElement(leId))
							if bface.GetBoundingElementFace().MaterialElementId.IntegerValue == -1: mlist.append(None)
							else: mlist.append(doc.GetElement(liId).GetLinkDocument().GetElement(bface.GetBoundingElementFace().MaterialElementId))
				else: 
					elist.append(doc.GetElement(eId))
					if bface.GetBoundingElementFace().MaterialElementId.IntegerValue == -1: mlist.append(None)
					else: mlist.append(doc.GetElement(bface.GetBoundingElementFace().MaterialElementId))
				alist.append(bface.GetSubface().Area)
				flist.append(bface.GetBoundingElementFace())
	except:
		pass	
	facetypes.append(tlist)
	facemats.append(mlist)
	faceelements.append(elist)
	faceareas.append(alist)
	faces.append(flist)
OUT = (facetypes,facemats,faceareas,faces,faceelements)