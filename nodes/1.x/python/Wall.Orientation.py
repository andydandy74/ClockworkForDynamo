import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

def WallOrientation(wall):
	loc = wall.Location
	if hasattr(loc, "Curve"):
		lcurve = loc.Curve
		if str(type(lcurve)) == "Autodesk.Revit.DB.Line":
			return wall.Orientation.ToVector()
		else:
			direction = (lcurve.GetEndPoint(1) - lcurve.GetEndPoint(0)).Normalize()
			return XYZ.BasisZ.CrossProduct(direction).ToVector()
	else: return None

walls = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [WallOrientation(x) for x in walls]
else: OUT = WallOrientation(walls)