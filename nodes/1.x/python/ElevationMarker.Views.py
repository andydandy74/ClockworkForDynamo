import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetElevationMarkerView(item):
	val = []
	if hasattr(item, "HasElevations"):
		if item.HasElevations():
			for i in range(item.MaximumViewCount):
				view = item.Document.GetElement(item.GetViewId(i))
				if view: val.append(view)
	return val

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetElevationMarkerView(x) for x in items]
else: OUT = GetElevationMarkerView(items)