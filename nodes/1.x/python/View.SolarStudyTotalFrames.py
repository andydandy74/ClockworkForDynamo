import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetFrameNum(view):
	if hasattr(view, 'SunAndShadowSettings'):
		if hasattr(view.SunAndShadowSettings, 'NumberOfFrames'): return view.SunAndShadowSettings.NumberOfFrames
		else: return 0
	else: return 0

views = UnwrapElement(IN[0])

if isinstance(views, list): OUT = [GetFrameNum(x) for x in views]
else: OUT = GetFrameNum(views)