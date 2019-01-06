import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])

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
				layerwidth.append(compstruc.GetLayerWidth(counter))
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