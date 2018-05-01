import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def HasVariableLayer(item):
	if hasattr(item, "GetCompoundStructure"):
		compstruc = item.GetCompoundStructure()
		if hasattr(compstruc, "VariableLayerIndex"):
			if compstruc.VariableLayerIndex == -1: return False
			else: return True
		else: return False
	else: return False

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [HasVariableLayer(x) for x in items]
else: OUT = HasVariableLayer(items)