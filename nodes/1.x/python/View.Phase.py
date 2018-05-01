import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetViewPhase(view):
	try: return view.Document.GetElement(view.get_Parameter(BuiltInParameter.VIEW_PHASE).AsElementId())
	except: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetViewPhase(x) for x in views]
else: OUT = GetViewPhase(views)