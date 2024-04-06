import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

items = UnwrapElement(IN[0])
paintedmats = IN[1]
version = IN[2]
if version > 2021: 
	unittypeA = ForgeTypeId('autodesk.spec.aec:area-2.0.0')
	unittypeV = ForgeTypeId('autodesk.spec.aec:volume-2.0.0')
else: 
	unittypeA = UnitType.UT_Area
	unittypeV = UnitType.UT_Volume

def InternalUnitToDisplayUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	if version > 2021: dispunits = formatoptions.GetUnitTypeId()
	else: dispunits = formatoptions.DisplayUnits
	try: return UnitUtils.ConvertFromInternalUnits(val,dispunits)
	except: return None
	
def ElementMaterials(item, painted):
	matlist = list()
	arealist = list()
	vollist = list()
	for matid in item.GetMaterialIds(painted):
		matlist.append(item.Document.GetElement(matid))
		arealist.append(InternalUnitToDisplayUnit(item.GetMaterialArea(matid,painted), unittypeA))
		vollist.append(InternalUnitToDisplayUnit(item.GetMaterialVolume(matid), unittypeV))
	return matlist, arealist, vollist, len(matlist) > 0

if isinstance(IN[0], list): 
	results = [ElementMaterials(x, paintedmats) for x in items]
	OUT = list(zip(*results))
else: OUT = ElementMaterials(items, paintedmats)