import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
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
		matlist.append(doc.GetElement(matid))
		arealist.append(item.GetMaterialArea(matid,paintedmats))
		vollist.append(item.GetMaterialVolume(matid))
	elementmats.append(matlist)
	elementareas.append(arealist)
	elementvols.append(vollist)
OUT = (elementmats,elementareas,elementvols)