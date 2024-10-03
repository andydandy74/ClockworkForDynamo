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
if version > 2021: unittype = ForgeTypeId('autodesk.spec.aec:length-2.0.0')
else: unittype = UnitType.UT_Length

def InternalUnitToDisplayUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	if version > 2021: dispunits = formatoptions.GetUnitTypeId()
	else: dispunits = formatoptions.DisplayUnits
	try: return UnitUtils.ConvertFromInternalUnits(val,dispunits)
	except: return None

OUT = (position_data.Angle, InternalUnitToDisplayUnit(position_data.Elevation, unittype), InternalUnitToDisplayUnit(position_data.EastWest, unittype), InternalUnitToDisplayUnit(position_data.NorthSouth, unittype))