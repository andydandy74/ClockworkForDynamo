import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetRooms(item, phase):
	if hasattr(item, "FromRoom") and str(phase.GetType()) == "Autodesk.Revit.DB.Phase":
		exits = 0
		if item.get_FromRoom(phase): exits += 1
		if item.get_ToRoom(phase): exits += 1
		return item.get_FromRoom(phase), item.get_ToRoom(phase), exits
	else: return None, None, 0

items = UnwrapElement(IN[0])
phase = UnwrapElement(IN[1])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetRooms(x, phase) for x in items]))
else: OUT = GetRooms(items, phase)