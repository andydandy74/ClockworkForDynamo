import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetViewScale(view):
	if hasattr(view, "Scale"): return view.Scale
	else: return None

views = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = [GetViewScale(x) for x in views]
else: OUT = GetViewScale(views)