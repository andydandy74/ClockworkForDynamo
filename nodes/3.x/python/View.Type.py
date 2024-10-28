import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetViewType(view):
	if hasattr(view, "ViewType"): return System.Enum.GetName(ViewType, view.ViewType)
	else: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0],list): OUT = [GetViewType(x) for x in views]
else: OUT = GetViewType(views)