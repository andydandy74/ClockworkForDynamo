import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetParamGUID(param):
	if hasattr(param, "GuidValue"): return param.GuidValue.ToString()
	else: return None
	
params = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetParamGUID(x) for x in params]
else: OUT = GetParamGUID(params)