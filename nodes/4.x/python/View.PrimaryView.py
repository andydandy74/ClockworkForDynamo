import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit

def GetPrimaryView(view):
	if hasattr(view, "GetPrimaryViewId"):
		return view.Document.GetElement(view.GetPrimaryViewId())
	else: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0], list):
	OUT = [GetPrimaryView(x) for x in views]
else:
	OUT = GetPrimaryView(views)