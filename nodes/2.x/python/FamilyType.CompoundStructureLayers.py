import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

items = UnwrapElement(IN[0])
version = IN[1]
if version > 2021: unittype = ForgeTypeId('autodesk.spec.aec:length-2.0.0')
else: unittype = UnitType.UT_Length

def InternalUnitToDisplayUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	if version > 2021: dispunits = formatoptions.GetUnitTypeId()
	else: dispunits = formatoptions.DisplayUnits
	try: return UnitUtils.ConvertFromInternalUnits(val,dispunits)
	except: return None

def GetCompoundStructureLayers(item):
	layers = []
	layermat = []
	layerfunc = []
	layerwidth = []
	layercore = []
	layerwraps = []
	layervar = []
	layerdeck = []	
	try:
		if hasattr(item, "GetCompoundStructure"):
			compstruc = item.GetCompoundStructure()
			vertcomp = compstruc.IsVerticallyCompound
			varlayer = compstruc.VariableLayerIndex
			num = compstruc.LayerCount
			counter = 0
			while counter < num:
				layers.append(compstruc.GetLayers()[counter])
				layermat.append(item.Document.GetElement(compstruc.GetMaterialId(counter)))
				layerfunc.append(compstruc.GetLayerFunction(counter))
				layerwidth.append(InternalUnitToDisplayUnit(compstruc.GetLayerWidth(counter), unittype))
				layercore.append(compstruc.IsCoreLayer(counter))
				if compstruc.IsCoreLayer(counter): layerwraps.append(False)
				else: layerwraps.append(compstruc.ParticipatesInWrapping(counter))
				if varlayer == counter: layervar.append(True)
				else: layervar.append(False)
				layerdeck.append(compstruc.IsStructuralDeck(counter))
				counter += 1
	except: pass
	return layers, layermat, layerfunc, layerwidth, layercore, layerwraps, layervar, layerdeck

if isinstance(IN[0], list): OUT = map(list, zip(*[GetCompoundStructureLayers(x) for x in items]))
else: OUT = GetCompoundStructureLayers(items)