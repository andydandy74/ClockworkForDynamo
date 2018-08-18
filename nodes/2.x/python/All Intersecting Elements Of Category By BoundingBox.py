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

doc = DocumentManager.Instance.CurrentDBDocument
cutters = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])
tol = IN[2]
cats = UnwrapElement(IN[3])

catlist = []
for cat in cats:
	catlist.append(cat.Id)
filtercats = List[ElementId](catlist)
catfilter = ElementMulticategoryFilter(filtercats)

intersectorlist = list()
for cutter in cutters:
	if cutter is None: intersectorlist.append([])
	else:
		bbox = cutter.get_BoundingBox(view)
		bboxfilter = BoundingBoxIntersectsFilter(Outline(bbox.Min,bbox.Max),tol)
		collector = FilteredElementCollector(doc, view.Id)
		excludelist = []
		excludelist.append(cutter.Id)
		excludeIDs = List[ElementId](excludelist)
		excfilter = ExclusionFilter(excludeIDs)
		intersectorlist.append(collector.WherePasses(bboxfilter).WherePasses(excfilter).WherePasses(catfilter).ToElements())
	
OUT = intersectorlist