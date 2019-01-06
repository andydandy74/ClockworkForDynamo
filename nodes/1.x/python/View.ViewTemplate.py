import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetViewTemplate(view):
	if not view: return None
	elif hasattr(view, "ViewTemplateId"):
		if view.ViewTemplateId.IntegerValue == -1: return None
		else: return view.Document.GetElement(view.ViewTemplateId)
	else: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetViewTemplate(x) for x in views]
else: OUT = GetViewTemplate(views)