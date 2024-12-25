import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetKeyScheduleParamName(schedule):
	try: return schedule.KeyScheduleParameterName
	except: return None

scheds = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetKeyScheduleParamName(x) for x in scheds]
else: OUT = GetKeyScheduleParamName(scheds)