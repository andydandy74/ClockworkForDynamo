import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetKeyScheduleParamName(schedule):
	if hasattr(schedule, "KeyScheduleParameterName"): return schedule.KeyScheduleParameterName
	else: return None

scheds = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetKeyScheduleParamName(x) for x in scheds]
else: OUT = GetKeyScheduleParamName(scheds)