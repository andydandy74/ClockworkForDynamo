import clr

import System
from System.Collections.Generic import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def DisplayUnitToInternalUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	if version > 2021: dispunits = formatoptions.GetUnitTypeId()
	else: dispunits = formatoptions.DisplayUnits
	try: return UnitUtils.ConvertToInternalUnits(val,dispunits)
	except: return None

def FindIntersects(item):
	if item is None: return []
	else:
		if view:
			bbox = item.get_BoundingBox(view)
			collector = FilteredElementCollector(doc, view.Id)
		else:
			bbox = item.get_BoundingBox(None)
			collector = FilteredElementCollector(doc)
		bboxfilter = BoundingBoxIntersectsFilter(Outline(bbox.Min,bbox.Max),tol)		
		excludelist = []
		excludelist.append(item.Id)
		excludeIDs = List[ElementId](excludelist)
		excfilter = ExclusionFilter(excludeIDs)
		return collector.WherePasses(bboxfilter).WherePasses(excfilter).WherePasses(catfilter).ToElements()

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])
version = IN[4]
filtercats = List[ElementId]([x.Id for x in IN[3]])
catfilter = ElementMulticategoryFilter(filtercats)
if version > 2021: unittype = ForgeTypeId('autodesk.spec.aec:length-2.0.0')
else: unittype = UnitType.UT_Length
tol = DisplayUnitToInternalUnit(IN[2], unittype)

if isinstance(IN[0], list): OUT = [FindIntersects(x) for x in items]
else: OUT = FindIntersects(items)