import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

def ViewDirection(view):
	if hasattr(view, "ViewDirection"):
		return view.ViewDirection.ToVector()
	else: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [ViewDirection(x) for x in views]
else: OUT = ViewDirection(views)