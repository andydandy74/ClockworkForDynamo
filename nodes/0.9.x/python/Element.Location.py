import clr
import math
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
pointlist = list()
curvepointlist = list()
ispoint = list()
iscurve = list()
curves = list()
haslocation = list()
angles, hasrotation = [], []

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
				angles.append(math.degrees(loc.Rotation) )
				ispoint.append(True)
				iscurve.append(False)
				angles.append
				haslocation.append(True)
				hasrotation.append(True)
			else:
				ispoint.append(False)
				iscurve.append(False)
				haslocation.append(False)
		except:
			try:
				# curves
				curvepoints = (item.GetEndPoint(0).ToPoint(),item.GetEndPoint(1).ToPoint())
				curvepointlist.append(curvepoints)
				curves.append(item.ToProtoType())
				ispoint.append(False)
				iscurve.append(True)
				haslocation.append(True)
			except:
				ispoint.append(False)
				iscurve.append(False)
				haslocation.append(False)
OUT = (pointlist,curvepointlist,curves,ispoint,iscurve,haslocation,angles, hasrotation)