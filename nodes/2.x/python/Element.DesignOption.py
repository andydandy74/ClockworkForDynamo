import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetDesignOption(item):
	if item:
		if hasattr(item, "DesignOption"): 
			return item.DesignOption
		else: return None
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetDesignOption(x) for x in items]
else: OUT = GetDesignOption(items)