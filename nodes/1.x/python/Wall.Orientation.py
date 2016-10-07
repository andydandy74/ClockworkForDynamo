import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

wallinstances = UnwrapElement(IN[0])
vectorlist = list()
for item in wallinstances:
	try:
		lcurve = item.Location.Curve
		if str(type(lcurve)) == "Autodesk.Revit.DB.Line":
			vectorlist.append(item.Orientation.ToVector())
		else:
			direction = (lcurve.GetEndPoint(1) - lcurve.GetEndPoint(0)).Normalize()
			vectorlist.append(XYZ.BasisZ.CrossProduct(direction))
	except:
		vectorlist.append(list())
OUT = vectorlist