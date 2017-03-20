import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

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
			try: 
				if g.Volume != 0:
					elementlist.append(g)
			except:
				pass
	return elementlist

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
detail_lvl = IN[1]
inc_invis = IN[2]
view = UnwrapElement(IN[3])
inserts = UnwrapElement(IN[4])
remove_inserts = IN[5]
revitlist = list()
dynlist = list()
# we might need a transaction in order to 
# temporarily delete all inserts and retrieve gross wall areas
TransactionManager.Instance.EnsureInTransaction(doc)
trans = SubTransaction(doc)
trans.Start()
i = 0
for item in items:
	if remove_inserts == True:
		for insert in inserts[i]:
			doc.Delete(insert.Id)
		doc.Regenerate()
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
			try:
				dyn_geos.append(geo.ToProtoType())
			except:
				pass
		dynlist.append(dyn_geos)	
	except:
		revitlist.append(list())
		dynlist.append(list())
	i += 1
trans.RollBack()
TransactionManager.Instance.TransactionTaskDone()
OUT = (dynlist,revitlist)