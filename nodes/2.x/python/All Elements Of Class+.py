import System
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def ElementsByType(etype, doc, schemaGUID):
	esFilter = None
	if schemaGUID: esFilter = ExtensibleStorage.ExtensibleStorageFilter(schemaGUID)
	# Special cases where we need to pull FamilyInstances first and then check against the desired type
	if str(etype) in ("Autodesk.Revit.DB.AnnotationSymbol", "Autodesk.Revit.DB.Mullion", "Autodesk.Revit.DB.Panel"):
		collector = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.FamilyInstance)
		if esFilter: collector = collector.WherePasses(esFilter)
		return [x for x in collector.ToElements() if x.GetType() == etype]
	# Special cases where we need to pull FamilySymbols first and then check against the desired type
	elif str(etype) in ("Autodesk.Revit.DB.AnnotationSymbolType", "Autodesk.Revit.DB.AreaTagType", "Autodesk.Revit.DB.Architecture.RoomTagType", "Autodesk.Revit.DB.Mechanical.SpaceTagType", "Autodesk.Revit.DB.Structure.TrussType"):
		collector = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.FamilySymbol)
		if esFilter: collector = collector.WherePasses(esFilter)
		return [x for x in collector.ToElements() if x.GetType() == etype]
	# Special cases where we need to pull SpatialElements first and then check against the desired type
	elif str(etype) in ("Autodesk.Revit.DB.Area", "Autodesk.Revit.DB.Architecture.Room", "Autodesk.Revit.DB.Mechanical.Space"):
		collector = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.SpatialElement)
		if esFilter: collector = collector.WherePasses(esFilter)
		return [x for x in collector.ToElements() if x.GetType() == etype]
	# Special cases where we need to pull SpatialElementTags first and then check against the desired type
	elif str(etype) in ("Autodesk.Revit.DB.AreaTag", "Autodesk.Revit.DB.Architecture.RoomTag", "Autodesk.Revit.DB.Mechanical.SpaceTag"):
		collector = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.SpatialElementTag)
		if esFilter: collector = collector.WherePasses(esFilter)
		return [x for x in collector.ToElements() if x.GetType() == etype]
	# Special cases where we need to pull CurveElements first and then check against the desired type
	elif str(etype) in ("Autodesk.Revit.DB.Structure.AreaReinforcementCurve", "Autodesk.Revit.DB.CurveByPoints", "Autodesk.Revit.DB.DetailArc", "Autodesk.Revit.DB.DetailCurve", "Autodesk.Revit.DB.DetailEllipse", "Autodesk.Revit.DB.DetailLine", "Autodesk.Revit.DB.DetailNurbSpline", "Autodesk.Revit.DB.ModelArc", "Autodesk.Revit.DB.ModelCurve", "Autodesk.Revit.DB.ModelEllipse", "Autodesk.Revit.DB.ModelHermiteSpline", "Autodesk.Revit.DB.ModelLine", "Autodesk.Revit.DB.ModelNurbSpline", "Autodesk.Revit.DB.SymbolicCurve"):
		collector = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.CurveElement)
		if esFilter: collector = collector.WherePasses(esFilter)
		return [x for x in collector.ToElements() if x.GetType() == etype]
	# Special cases where we need to pull HostedSweep first and then check against the desired type
	if str(etype) in ("Autodesk.Revit.DB.Architecture.Fascia", "Autodesk.Revit.DB.Architecture.Gutter", "Autodesk.Revit.DB.SlabEdge"):
		collector = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.HostedSweep)
		if esFilter: collector = collector.WherePasses(esFilter)
		return [x for x in collector.ToElements() if x.GetType() == etype]
	else:
		try:
			collector = FilteredElementCollector(doc).OfClass(etype)
			if esFilter: collector = collector.WherePasses(esFilter)
			return collector.ToElements()
		except: return None

inputdoc = UnwrapElement(IN[2])
if not inputdoc: doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document": doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument
schemaGUID = IN[3]

if isinstance(IN[0], list): OUT = [ElementsByType(x, doc, schemaGUID) for x in IN[0]]
else: OUT = ElementsByType(IN[0], doc, schemaGUID)