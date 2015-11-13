import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elemlayers = list()
elemmat = list()
elemfunc = list()
elemwidth = list()
elemcore = list()
elemwraps = list()
elemvar = list()
elemdeck = list()

for item in items:
	try:
		counter = 0
		layers = list()
		layermat = list()
		layerfunc = list()
		layerwidth = list()
		layercore = list()
		layerwraps = list()
		layervar = list()
		layerdeck = list()
		compstruc = item.GetCompoundStructure()
		num = compstruc.LayerCount
		vertcomp = compstruc.IsVerticallyCompound
		varlayer = compstruc.VariableLayerIndex
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
	except:
		pass
	elemlayers.append(layers)
	elemmat.append(layermat)
	elemfunc.append(layerfunc)
	elemwidth.append(layerwidth)
	elemcore.append(layercore)
	elemwraps.append(layerwraps)
	elemvar.append(layervar)
	elemdeck.append(layerdeck)
OUT = (elemlayers, elemmat, elemfunc, elemwidth, elemcore, elemwraps, elemvar, elemdeck)