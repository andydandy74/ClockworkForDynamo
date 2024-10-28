import clr
import System
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
unittype = ForgeTypeId('autodesk.spec.aec:length-2.0.0')

def InternalUnitToDisplayUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	dispunits = formatoptions.GetUnitTypeId()
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
	if hasattr(item, "GetCompoundStructure"):
		compstruc = item.GetCompoundStructure()
		if compstruc:
			vertcomp = compstruc.IsVerticallyCompound
			varlayer = compstruc.VariableLayerIndex
			num = compstruc.LayerCount
			counter = 0
			while counter < num:
				layers.append(compstruc.GetLayers()[counter])
				layermat.append(item.Document.GetElement(compstruc.GetMaterialId(counter)))
				layerfunc.append(System.Enum.GetName(MaterialFunctionAssignment, compstruc.GetLayerFunction(counter)))
				layerwidth.append(InternalUnitToDisplayUnit(compstruc.GetLayerWidth(counter), unittype))
				layercore.append(compstruc.IsCoreLayer(counter))
				if compstruc.IsCoreLayer(counter): layerwraps.append(False)
				else: layerwraps.append(compstruc.ParticipatesInWrapping(counter))
				if varlayer == counter: layervar.append(True)
				else: layervar.append(False)
				layerdeck.append(compstruc.IsStructuralDeck(counter))
				counter += 1
	return layers, layermat, layerfunc, layerwidth, layercore, layerwraps, layervar, layerdeck

if isinstance(IN[0], list): OUT = map(list, zip(*[GetCompoundStructureLayers(x) for x in items]))
else: OUT = GetCompoundStructureLayers(items)