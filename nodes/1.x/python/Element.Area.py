import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetArea(spatialElement):
	if hasattr(spatialElement, "Area"): return spatialElement.Area
	else: return None

spatialElements = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetArea(x) for x in spatialElements]
else: OUT = GetArea(spatialElements)