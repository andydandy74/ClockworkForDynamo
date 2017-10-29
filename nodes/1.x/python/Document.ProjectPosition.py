import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

inputdoc = UnwrapElement(IN[1])
version = IN[2]
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

projloc = doc.ActiveProjectLocation
if version > 2017:
	position_data = projloc.GetProjectPosition(XYZ.Zero)
	location_data = projloc.GetSiteLocation()
else:
	position_data = projloc.ProjectPosition[XYZ.Zero]
	location_data = projloc.SiteLocation
OUT = (position_data.Angle,position_data.Elevation,position_data.EastWest,position_data.NorthSouth)