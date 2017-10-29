import clr
import math
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
pointlist, curvepointlist, ispoint, iscurve, curves, haslocation, angles, hasrotation = [], [], [], [], [], [], [], []

for item in items:
	try:
		# points and text notes
		pointlist.append(item.Coord.ToPoint())
		ispoint.append(True)
		iscurve.append(False)
		haslocation.append(True)
		hasrotation.append(False)
	except:
		try:
			loc = item.Location
			if loc.ToString() == 'Autodesk.Revit.DB.LocationCurve':
				# line-based elements (e.g. walls)
				curvepoints = (loc.Curve.GetEndPoint(0).ToPoint(),loc.Curve.GetEndPoint(1).ToPoint())
				curvepointlist.append(curvepoints)
				curves.append(loc.Curve.ToProtoType())
				ispoint.append(False)
				iscurve.append(True)
				haslocation.append(True)
				hasrotation.append(False)
			elif loc.ToString() == 'Autodesk.Revit.DB.LocationPoint':
				# point-based elements
				pointlist.append(loc.Point.ToPoint())
				ispoint.append(True)
				iscurve.append(False)
				haslocation.append(True)
				try:
					angles.append(math.degrees(loc.Rotation))
					hasrotation.append(True)
				except:
					hasrotation.append(False)
			else:
				# check for host objects outlines (floor slabs etc.)
				try:
					refs = HostObjectUtils.GetTopFaces(item)
					blines = []
					bpoints = []
					for ref in refs:
						try:
							boundaries = item.GetGeometryObjectFromReference(ref).GetEdgesAsCurveLoops()
							for loop in boundaries:
								cloop = []
								clooppoints = []
								for line in loop:
									cloop.append(line.ToProtoType())
									curvepoint = (line.GetEndPoint(0).ToPoint(),line.GetEndPoint(1).ToPoint())
									clooppoints.append(curvepoint)
								blines.append(cloop)
								bpoints.append(clooppoints)
						except:
							pass
					if (len(blines) > 0):
						curves.append(blines)
						curvepointlist.append(bpoints)
						iscurve.append(True)
						haslocation.append(True)
					else:
						iscurve.append(False)
						haslocation.append(False)
					ispoint.append(False)
					hasrotation.append(False)
				except:
					ispoint.append(False)
					iscurve.append(False)
					haslocation.append(False)
					hasrotation.append(False)
		except:
			try:
				# curves
				curvepoints = (item.GetEndPoint(0).ToPoint(),item.GetEndPoint(1).ToPoint())
				curvepointlist.append(curvepoints)
				curves.append(item.ToProtoType())
				ispoint.append(False)
				iscurve.append(True)
				haslocation.append(True)
				hasrotation.append(False)
			except:
				ispoint.append(False)
				iscurve.append(False)
				haslocation.append(False)
				hasrotation.append(False)
OUT = (pointlist,curvepointlist,curves,ispoint,iscurve,haslocation,angles,hasrotation)