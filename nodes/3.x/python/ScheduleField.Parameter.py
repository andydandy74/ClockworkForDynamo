import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetScheduleFieldParam(schedulefield):
	if hasattr(schedulefield, "ParameterId"): 
		pId = schedulefield.ParameterId
		if pId != ElementId.InvalidElementId: 
			# BuiltInParameters
			if pId.IntegerValue < 0: 
				try: return bips[bipIds.index(pId.IntegerValue)]
				except: return None
			# Project/Family/Shared Parameters
			else: return schedulefield.Schedule.Document.GetElement(schedulefield.ParameterId)
		else: return None
	else: return None

schedulefields = UnwrapElement(IN[0])
bipsAll = System.Enum.GetValues(BuiltInParameter)
bips = []
bipIds = []
for bip in bipsAll:
	try:
		bips.append(bip)
		bipIds.append(ElementId(bip).IntegerValue)
	except: pass

if isinstance(IN[0], list): OUT = [GetScheduleFieldParam(x) for x in schedulefields]
else: OUT = GetScheduleFieldParam(schedulefields)