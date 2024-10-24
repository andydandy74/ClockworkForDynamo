import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

spatialElements = UnwrapElement(IN[0])
unittype = ForgeTypeId('autodesk.spec.aec:area-2.0.0')

def InternalUnitToDisplayUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	dispunits = formatoptions.GetUnitTypeId()
	try: return UnitUtils.ConvertFromInternalUnits(val,dispunits)
	except: return None
	
def GetArea(spatialElement):
	if hasattr(spatialElement, "Area"): return InternalUnitToDisplayUnit(spatialElement.Area, unittype)
	else: return None

if isinstance(IN[0], list): OUT = [GetArea(x) for x in spatialElements]
else: OUT = GetArea(spatialElements)