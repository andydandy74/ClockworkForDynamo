import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

def ViewPlane(view):
	if hasattr(view, "ViewDirection") and hasattr(view, "Origin"):
		o = view.Origin
		n = view.ViewDirection
		if o and n: return Plane.ByOriginNormal(o.ToPoint(), n.ToVector())
		else: return None
	else: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [ViewPlane(x) for x in views]
else: OUT = ViewPlane(views)