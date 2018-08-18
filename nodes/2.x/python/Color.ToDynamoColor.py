import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetColorComponents(color):
	if hasattr(color, "Red") and hasattr(color, "Blue") and hasattr(color, "Green"): return color.Red, color.Green, color.Blue
	else: return None, None, None

colors = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetColorComponents(x) for x in colors]))
else: OUT = GetColorComponents(colors)