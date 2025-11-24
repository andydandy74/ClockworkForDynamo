import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetFamParamProperties(param):
	try: guid = param.GUID.ToString()
	except: guid = None
	try: dutype = param.GetUnitTypeId()
	except: dutype = None
	assocparams = param.AssociatedParameters
	assocelems = list()
	for assoc in assocparams:
		assocelems.append(assoc.Element)
	return param.Definition.Name, guid, param.Definition.GetGroupTypeId(), param.Definition.GetDataType(), dutype, System.Enum.GetName(StorageType, param.StorageType), param.IsInstance, param.IsReporting, param.IsShared, param.IsReadOnly, param.UserModifiable, param.Formula, param.IsDeterminedByFormula, assocparams, param.CanAssignFormula, assocelems

params = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = list(zip(*[GetFamParamProperties(x) for x in params]))
else: OUT = GetFamParamProperties(params)

##### NEXT PYTHON NODE #####

import clr
OUT = []
for chunks in IN[0]:
	sublist = []
	if chunks: [sublist.append(x) for x in chunks if x in IN[1]]
	OUT.append(sublist)
	