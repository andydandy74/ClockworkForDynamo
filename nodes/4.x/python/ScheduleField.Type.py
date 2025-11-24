import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetScheduleFieldType(field):
	if hasattr(field, "FieldType"): return System.Enum.GetName(ScheduleFieldType, field.FieldType)
	else: return None

if isinstance(IN[0], list): OUT = [GetScheduleFieldType(x) for x in IN[0]]
else: OUT = GetScheduleFieldType(IN[0])