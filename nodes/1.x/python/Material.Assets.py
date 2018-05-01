import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

mats = UnwrapElement(IN[0])

def GetMaterialAssets(material):
	if material: return (material.Document.GetElement(material.AppearanceAssetId), material.Document.GetElement(material.ThermalAssetId), material.Document.GetElement(material.StructuralAssetId))
	else: return (None, None, None)

OUT = map(list, zip(*[GetMaterialAssets(x) for x in mats]))