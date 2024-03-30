import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetHost(item):
	# standard
	if hasattr(item, "Host"): return item.Host
	# Wall sweeps
	elif hasattr(item, "GetHostIds"): return [item.Document.GetElement(x) for x in item.GetHostIds()]
	# Wall foundations
	elif hasattr(item, "WallId"): return item.Document.GetElement(item.WallId)
	# railings, building pads
	elif hasattr(item, "HostId"): return item.Document.GetElement(item.HostId)
	# topo subregions
	elif hasattr(item, "AsSiteSubRegion"): return item.Document.GetElement(item.AsSiteSubRegion().HostId)	
	# topo solids
	elif hasattr(item, "HostTopoId"): return item.Document.GetElement(item.HostTopoId)
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetHost(x) for x in items]
else: OUT = GetHost(items)