import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetRooms(item, phase):
	if hasattr(item, "FromRoom") and str(phase.GetType()) == "Autodesk.Revit.DB.Phase":
		exits = 0
		# Need to wrap this in try/except for doors/windows that don't exist in the given phase
		try: 
			if item.FromRoom[phase]: exits += 1
			if item.ToRoom[phase]: exits += 1
			return item.FromRoom[phase], item.ToRoom[phase], exits
		except:
			return None, None, 0
	else: return None, None, 0

items = UnwrapElement(IN[0])
phase = UnwrapElement(IN[1])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetRooms(x, phase) for x in items]))
else: OUT = GetRooms(items, phase)