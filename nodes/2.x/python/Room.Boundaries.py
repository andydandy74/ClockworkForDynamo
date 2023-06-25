import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("System")
from System.Collections.Generic import List

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
	# 1st pass - low hanging fruit
	try:
		for boundarylist in item.GetBoundarySegments(options):
			for boundary in boundarylist:
				# fix possibly missing bounding element in previous entry
				if len(elements) > 2:
					if elements[-1] == None:
						# simple case: front face of wall protruding into room
						if boundary.ElementId == elements[-2].Id: 
							elements[-1] = doc.GetElement(boundary.ElementId)
				# add boundary to list
				elements.append(doc.GetElement(boundary.ElementId))
				if version > 2016: curves.append(boundary.GetCurve())
				else: curves.append(boundary.Curve)
	except: pass
	# 2nd pass - special cases (if any)
	if None in elements:
		elementset = set(elements)
		elementset.remove(None)
		i = 0
		for e, c in zip(elements, curves):
			if e == None:
				p = c.ComputeDerivatives(0.5, True).Origin.Add(XYZ(0,0,1))
				bbox = BoundingBoxXYZ()
				bbox.Min = p.Subtract(bboxVec)
				bbox.Max = p.Add(bboxVec)
				bboxFilter = BoundingBoxIntersectsFilter(Outline(bbox.Min,bbox.Max))
				collector = FilteredElementCollector(doc)
				results = collector.WherePasses(bboxFilter).WherePasses(catFilter).ToElements()
				if len(results) > 0: elements[i] = results[0]				
			i += 1
	rcurves = [x.ToProtoType() for x in curves]
	return elements, rcurves

items = UnwrapElement(IN[0])

bics = [BuiltInCategory.OST_Walls, BuiltInCategory.OST_StructuralColumns, BuiltInCategory.OST_Columns]
bicCol = List[BuiltInCategory](bics)
catFilter = ElementMulticategoryFilter(bicCol)
bboxVec = XYZ(0.01,0.01,0.01)

if isinstance(IN[0], list): OUT = map(list, zip(*[GetRoomBoundaries(x, IN[1]) for x in items]))
else: OUT = GetRoomBoundaries(items, IN[1])