import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# this function takes care of exploding 
# GeometryInstance objects. GI objects typically
# represent family instance geometry.
# in order to also catch possible nested families
# the fucntion calls itself recursively.
def convert_geometry_instance(geo, elementlist):
	for g in geo:
		if str(g.GetType()) == 'Autodesk.Revit.DB.GeometryInstance':
			elementlist = convert_geometry_instance(g.GetInstanceGeometry(), elementlist)
		else:
			elementlist.append(g)
	return elementlist

items = UnwrapElement(IN[0])
detail_lvl = IN[1]
inc_invis = IN[2]
view = UnwrapElement(IN[3])
revitlist = list()
dynlist = list()
for item in items:
	geo_options = Options()
	if view == None: geo_options.DetailLevel = detail_lvl
	geo_options.IncludeNonVisibleObjects = inc_invis
	if view != None: geo_options.View = view
	revitGeo = item.Geometry[geo_options]
	try:
		
		revit_geos = convert_geometry_instance(revitGeo, list())
		revitlist.append(revit_geos)
		dyn_geos = list()
		for geo in revit_geos:
			dyn_geos.append(geo.ToProtoType())
		dynlist.append(dyn_geos)	
	except:
		revitlist.append(list())
		dynlist.append(list())
OUT = (dynlist,revitlist)