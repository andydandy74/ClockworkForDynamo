import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def DisplayUnitToInternalUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	if version > 2021: dispunits = formatoptions.GetUnitTypeId()
	else: dispunits = formatoptions.DisplayUnits
	try: return UnitUtils.ConvertToInternalUnits(val,dispunits)
	except: return None

def SetCompoundLayerWidth(famtype, index, width):
	try:
		cs = famtype.GetCompoundStructure()
		cs.SetLayerWidth(index, DisplayUnitToInternalUnit(width, unittype))
		famtype.SetCompoundStructure(cs)
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument
famtypes = UnwrapElement(IN[0])
indices = IN[1]
widths = IN[2]
version = IN[3]
if version > 2021: unittype = ForgeTypeId('autodesk.spec.aec:length-2.0.0')
else: unittype = UnitType.UT_Length

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[2], list):
		if isinstance(IN[1], list): OUT = [SetCompoundLayerWidth(x,y,z) for x,y,z in zip(famtypes, indices, widths)]
		else: OUT = [SetCompoundLayerWidth(x,indices,y) for x,y in zip(famtypes, widths)]
	else:
		if isinstance(IN[1], list): OUT = [SetCompoundLayerWidth(x,y,widths) for x,y in zip(famtypes, indices)]
		else: OUT = [SetCompoundLayerWidth(x,indices,widths) for x in famtypes]
else:
	if isinstance(IN[2], list):
		if isinstance(IN[1], list): OUT = [SetCompoundLayerWidth(famtypes,x,y) for x,y in zip(indices, widths)]
		else: OUT = [SetCompoundLayerWidth(famtypes,indices,x) for x in widths]
	else:
		if isinstance(IN[1], list): OUT = [SetCompoundLayerWidth(famtypes,x,widths) for x in indices]
		else: OUT = SetCompoundLayerWidth(famtypes,indices,widths)
TransactionManager.Instance.TransactionTaskDone()