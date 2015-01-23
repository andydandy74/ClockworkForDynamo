import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

projloc = doc.ActiveProjectLocation
position_data = projloc.ProjectPosition[XYZ.Zero]
location_data = projloc.SiteLocation
OUT = (position_data.Angle,position_data.Elevation,position_data.EastWest,position_data.NorthSouth, location_data.Latitude, location_data.Longitude)