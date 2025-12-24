import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetScheduleFieldParam(schedulefield):
    if hasattr(schedulefield, "ParameterId"): 
        pId = schedulefield.ParameterId
        if pId != ElementId.InvalidElementId: 
            pIdVal = pId.Value
            # BuiltInParameters
            if pIdVal < 0: 
                try: return System.Enum.GetName(BuiltInParameter, pIdVal)
                except: return None
            # Project/Family/Shared Parameters
            else: return schedulefield.Schedule.Document.GetElement(schedulefield.ParameterId)
        else: return None
    else: return None

schedulefields = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetScheduleFieldParam(x) for x in schedulefields]
else: OUT = GetScheduleFieldParam(schedulefields)