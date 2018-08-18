import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

def WallOrientation(wall):
	loc = wall.Location
	flipped = False
	if hasattr(loc, "Curve"):
		lcurve = loc.Curve
		if hasattr(wall, "Flipped"): flipped = wall.Flipped
		if str(type(lcurve)) == "Autodesk.Revit.DB.Line":
			if flipped: return wall.Orientation.ToVector().Reverse()
			else: return wall.Orientation.ToVector()
		else:
			direction = (lcurve.GetEndPoint(1) - lcurve.GetEndPoint(0)).Normalize()
			if flipped: return XYZ.BasisZ.CrossProduct(direction).ToVector().Reverse()
			else: return XYZ.BasisZ.CrossProduct(direction).ToVector()
	else: return None

walls = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [WallOrientation(x) for x in walls]
else: OUT = WallOrientation(walls)