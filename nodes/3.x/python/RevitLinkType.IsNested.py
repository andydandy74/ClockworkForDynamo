import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

links = UnwrapElement(IN[0])

def IsNested(link):
	if hasattr(link, "IsNestedLink"): return link.IsNestedLink
	else: return None

if isinstance(IN[0], list): OUT = [IsNested(x) for x in links]
else: OUT = IsNested(links)