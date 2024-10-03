import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

mats = UnwrapElement(IN[0])

def GetMaterialAssets(material):
	if hasattr(material, "AppearanceAssetId"): return (material.Document.GetElement(material.AppearanceAssetId), material.Document.GetElement(material.ThermalAssetId), material.Document.GetElement(material.StructuralAssetId))
	else: return (None, None, None)

if isinstance(IN[0], list): OUT = map(list, zip(*[GetMaterialAssets(x) for x in mats]))
else: OUT = GetMaterialAssets(mats)