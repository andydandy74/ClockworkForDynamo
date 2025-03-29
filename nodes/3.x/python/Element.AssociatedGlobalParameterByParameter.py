import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetAssociatedGlobalParam(item, param):
	rparams = item.GetParameters(param)
	if len(rparams) > 0: 
		return item.Document.GetElement(rparams[0].GetAssociatedGlobalParameter())
	else: return None

items = UnwrapElement(IN[0])
params = IN[1]

if isinstance(IN[0], list): 
	if isinstance(IN[1], list): OUT = [GetAssociatedGlobalParam(x, y) for x, y in zip(items, params)]
	else: OUT = [GetAssociatedGlobalParam(x, params) for x in items]
else: 
	if isinstance(IN[1], list): OUT = [GetAssociatedGlobalParam(items, x) for x in params]
	else: OUT = GetAssociatedGlobalParam(items, params)