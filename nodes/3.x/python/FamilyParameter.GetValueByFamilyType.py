import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

def GetFamParamVal(ft, fp):
	if fp.StorageType == StorageType.Integer: return ft.AsInteger(fp)
	elif fp.StorageType == StorageType.Double: 
		if version > 2021:
			if fp.GetUnitTypeId() and ft.HasValue(fp): return UnitUtils.ConvertFromInternalUnits(ft.AsDouble(fp),fp.GetUnitTypeId())
			else: return ft.AsDouble(fp)
		else:
			if fp.DisplayUnitType and ft.HasValue(fp): return UnitUtils.ConvertFromInternalUnits(ft.AsDouble(fp),fp.DisplayUnitType)
			else: return ft.AsDouble(fp)
	elif fp.StorageType == StorageType.String: return ft.AsString(fp)
	elif fp.StorageType == StorageType.ElementId: return doc.GetElement(ft.AsElementId(fp))
	else: return None

version = IN[2]
if isinstance(IN[0], list): 
	if isinstance(IN[1], list): 
		OUT = []
		OUT = [[GetFamParamVal(y, x) for x in IN[1]] for y in IN[0]]
	else: OUT = [GetFamParamVal(x, IN[1]) for x in IN[0]]
else:
	if isinstance(IN[1], list): OUT = [GetFamParamVal(IN[0], x) for x in IN[1]]
	else: OUT = GetFamParamVal(IN[0], IN[1])