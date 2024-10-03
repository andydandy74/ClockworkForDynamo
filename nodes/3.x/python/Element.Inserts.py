import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
incopenings = IN[1]
incshadows = IN[2]
incwalls = IN[3]
incshared = IN[4]

def GetInserts(item,incopenings,incshadows,incwalls,incshared):
	# Regular host objects
	if hasattr(item, "FindInserts"):
		return [item.Document.GetElement(x) for x in item.FindInserts(incopenings,incshadows,incwalls,incshared)]
	# Railings
	elif hasattr(item, "GetAssociatedRailings"):
		return [item.Document.GetElement(x) for x in item.GetAssociatedRailings()]
	else: return []

if isinstance(IN[0], list): OUT = [GetInserts(x,incopenings,incshadows,incwalls,incshared) for x in items]
else: OUT = GetInserts(items,incopenings,incshadows,incwalls,incshared)