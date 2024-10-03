import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsViewTemplate(view):
	if hasattr(view, "IsTemplate"): return view.IsTemplate
	else: return False

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsViewTemplate(x) for x in views]
else: OUT = IsViewTemplate(views)