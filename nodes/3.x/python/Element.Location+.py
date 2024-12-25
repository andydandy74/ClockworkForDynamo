import clr
import math
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

items = UnwrapElement(IN[0])

def GetCurvePoints(curve):
	return curve.GetEndPoint(0).ToPoint(), curve.GetEndPoint(1).ToPoint()

def GetLocation(item):
	# returns the following properties:
	# [0] point
	# [1] curve
	# [2] is point?
	# [3] is curve?
	# [4] has location?
	# [5] rotation angle
	# [6] has rotation?
	# [7] is curve loop?
	# [8] curve loop
	# default values
	point = None
	curveendpoints = None
	curve = None
	ispoint = False
	iscurve = False
	haslocation = False
	rotationangle = None
	hasrotation = False
	iscurveloop = False
	curveloop = None
	# template for return statements:
	# return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop
	# points and text notes
	if hasattr(item, "Coord"): 
		return item.Coord.ToPoint(), curveendpoints, curve, True, iscurve, True, rotationangle, hasrotation, iscurveloop, curveloop
	# base points and reference points
	if hasattr(item, "Position"): 
		return item.Position.ToPoint(), curveendpoints, curve, True, iscurve, True, rotationangle, hasrotation, iscurveloop, curveloop
	# independent tags
	if hasattr(item, "TagHeadPosition") and hasattr(item, "IsMaterialTag"): 
		return item.TagHeadPosition.ToPoint(), curveendpoints, curve, True, iscurve, True, rotationangle, hasrotation, iscurveloop, curveloop
	# views
	if hasattr(item, "ViewType") and hasattr(item, "Origin"): 
		ori = item.Origin
		if ori: return ori.ToPoint(), curveendpoints, curve, True, iscurve, True, rotationangle, hasrotation, iscurveloop, curveloop
		else: return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop
	# stair runs and landings
	if hasattr(item, "GetFootprintBoundary"):
		footprint = [x.ToProtoType() for x in item.GetFootprintBoundary()]
		return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, footprint
	# grids, dimensions and boundary segments
	elif hasattr(item, "Curve"): 
		return point, GetCurvePoints(item.Curve), item.Curve.ToProtoType(), ispoint, True, True, rotationangle, hasrotation, iscurveloop, curveloop
	# curtain grid lines
	elif hasattr(item, "FullCurve"): 
		return point, GetCurvePoints(item.FullCurve), item.FullCurve.ToProtoType(), ispoint, True, True, rotationangle, hasrotation, iscurveloop, curveloop
	# curves
	elif hasattr(item, "GetEndpoint"): 
		return point, GetCurvePoints(item), item.ToProtoType(), ispoint, True, True, rotationangle, hasrotation, iscurveloop, curveloop
	# railings and top rails
	elif hasattr(item, "GetPath"):
		railpath = []
		for x in item.GetPath():
			try: railpath.append(x.ToProtoType())
			except: pass
		# paths with multiple segments
		if len(railpath) > 1: return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, railpath
		# paths with a single segment
		elif len(railpath) == 1: return point, GetCurvePoints(railpath[0].ToRevitType()), railpath[0], ispoint, True, True, rotationangle, hasrotation, iscurveloop, curveloop
		# paths without legible segments
		else: return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop
	# openings
	elif hasattr(item, "BoundaryCurves"):
		# rectangular openings
		if item.IsRectBoundary:
			zVals = [x.Z for x in item.BoundaryRect]
			p = []
			for o in item.BoundaryRect:
				for z in zVals: p.append(XYZ(o.X, o.Y, z).ToPoint())
			rectloop = Rectangle.ByCornerPoints(p[0], p[1], p[3], p[2]).Explode()
			return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, rectloop
		# none-rectangular openings
		else: 
			openingloop = [x.ToProtoType() for x in item.BoundaryCurves]
			return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, openingloop
	# extrusion roofs
	elif hasattr(item, "GetProfile"):
		sketchloop = [x.GeometryCurve.ToProtoType() for x in item.GetProfile()]
		return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, sketchloop
	# newer sketch-based elements (except walls)
	elif hasattr(item, "SketchId") and not hasattr(item, "WallType"):
		sketch = item.Document.GetElement(item.SketchId)
		if sketch:
			sketchloop = []
			for loop in sketch.Profile:
				sketchloop.append([x.ToProtoType() for x in loop])
			return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, sketchloop
		else: return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop
	# other elements
	elif hasattr(item, "Location"):
		loc = item.Location
		if loc:
			# line-based elements (e.g. walls)
			if loc.ToString() == 'Autodesk.Revit.DB.LocationCurve':
				#loc.Curve.ToProtoType()
				try: return point, GetCurvePoints(loc.Curve), loc.Curve.ToProtoType(), ispoint, True, True, rotationangle, hasrotation, iscurveloop, curveloop
				# return super short curves as startpoint instead
				except: return GetCurvePoints(loc.Curve)[0], curveendpoints, curve, True, iscurve, True, rotationangle, hasrotation, iscurveloop, curveloop
			# point-based elements (e.g. most loadable families)
			elif loc.ToString() == 'Autodesk.Revit.DB.LocationPoint':
				try:
					if hasattr(loc, "Rotation"):
						rotationangle = math.degrees(loc.Rotation)
						hasrotation = True
				except: pass
				return loc.Point.ToPoint(), curveendpoints, curve, True, iscurve, True, rotationangle, hasrotation, iscurveloop, curveloop
			# some elements have a location property but don't return curves or points
			else:
				# earlier sketch-based elements (e.g. floor slabs)
				try:
					sketchloop = []
					for ref in HostObjectUtils.GetTopFaces(item):
						geomref = item.GetGeometryObjectFromReference(ref)
						if geomref: 
							boundaryloops = geomref.GetEdgesAsCurveLoops()
							for loop in boundaryloops:
								sketchloop.append([x.ToProtoType() for x in loop])
					return point, curveendpoints, curve, ispoint, iscurve, True, rotationangle, hasrotation, True, sketchloop
				# other elements we can't process
				# return defaults in these cases
				except:
					return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop
		# some elements (e.g.groups, curtain panels etc.)  have a location property which only returns a NoneType
		# return defaults in these cases
		else: return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop
	# in all other cases return defaults
	else: return point, curveendpoints, curve, ispoint, iscurve, haslocation, rotationangle, hasrotation, iscurveloop, curveloop

if isinstance(IN[0], list):
	locations = [GetLocation(x) for x in items]
	# Transpose and remove NoneTypes
	OUT = []
	for prop in map(list, zip(*locations)):
		OUT.append(filter(lambda x: x!=None, prop))
else: OUT = GetLocation(items)