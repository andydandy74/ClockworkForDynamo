import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

links = UnwrapElement(IN[0])

def GetPathType(link):
	if hasattr(link, "PathType"): return link.PathType.ToString()
	else: return None

if isinstance(IN[0], list): OUT = [GetPathType(x) for x in links]
else: OUT = GetPathType(links)