import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
paintedmats = IN[1]
elementmats = list()
elementareas = list()
elementvols = list()

for item in items:
	matlist = list()
	arealist = list()
	vollist = list()
	for matid in item.GetMaterialIds(paintedmats):
		matlist.append(item.Document.GetElement(matid))
		arealist.append(item.GetMaterialArea(matid,paintedmats))
		vollist.append(item.GetMaterialVolume(matid))
	elementmats.append(matlist)
	elementareas.append(arealist)
	elementvols.append(vollist)
OUT = (elementmats,elementareas,elementvols)