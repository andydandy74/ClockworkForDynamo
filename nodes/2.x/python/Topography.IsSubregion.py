import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsTopoSubregion(topo):
	if hasattr(topo, "IsSiteSubRegion"): return topo.IsSiteSubRegion
	else: return False

topos = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsTopoSubregion(x) for x in topos]
else: OUT = IsTopoSubregion(topos)