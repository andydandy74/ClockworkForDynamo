import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetName(item):
	unwrapped = UnwrapElement(item)
	if not unwrapped: return None
	elif unwrapped.GetType().ToString() in ("Autodesk.Revit.DB.BuiltInParameter", "Autodesk.Revit.DB.BuiltInParameterGroup", "Autodesk.Revit.DB.DisplayUnitType", "Autodesk.Revit.DB.ParameterType", "Autodesk.Revit.DB.UnitSymbolType", "Autodesk.Revit.DB.UnitType"): return LabelUtils.GetLabelFor(unwrapped)
	elif unwrapped.GetType().ToString() in ("Autodesk.Revit.DB.Parameter", "Autodesk.Revit.DB.FamilyParameter"): return unwrapped.Definition.Name
	elif hasattr(unwrapped, "Name"): return unwrapped.Name
	elif hasattr(item, "Name"): return item.Name
	else: return None

items = IN[0]

if isinstance(IN[0], list): OUT = [GetName(x) for x in IN[0]]
else: OUT = GetName(IN[0])