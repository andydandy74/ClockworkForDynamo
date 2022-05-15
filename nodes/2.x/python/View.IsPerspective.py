import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def ViewIsPerspective(view):
	if hasattr(view, "IsPerspective"): return view.IsPerspective
	else: return False

views = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = [ViewIsPerspective(x) for x in views]
else: OUT = ViewIsPerspective(views)