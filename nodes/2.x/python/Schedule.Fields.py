import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetScheduleFields(schedule):
	if hasattr(schedule, "Definition"): 
		return [schedule.Definition.GetField(x) for x in schedule.Definition.GetFieldOrder()]
	else: return []

scheds = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetScheduleFields(x) for x in scheds]
else: OUT = GetScheduleFields(scheds)