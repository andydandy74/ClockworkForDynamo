import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

params = UnwrapElement(IN[0])
pname = list()
guid = list()
pgroup = list()
ptype = list()
utype = list()
dutype = list()
stype = list()
isinstance = list()
isreporting = list()
isshared = list()
isreadonly = list()
usermodifiable = list()
formula = list()
determinedbyformula = list()
associatedparams = list()
associatedelements = list()
canassignformula = list()
for param in params:
	pname.append(param.Definition.Name)
	try:guid.append(param.GUID)
	except: guid.append(None)
	pgroup.append(param.Definition.ParameterGroup)
	ptype.append(param.Definition.ParameterType)
	utype.append(param.Definition.UnitType)
	try: dutype.append(param.DisplayUnitType)
	except: dutype.append(None)
	stype.append(param.StorageType)
	isinstance.append(param.IsInstance)
	isreporting.append(param.IsReporting)
	isshared.append(param.IsShared)
	isreadonly.append(param.IsReadOnly)
	usermodifiable.append(param.UserModifiable)
	formula.append(param.Formula)
	determinedbyformula.append(param.IsDeterminedByFormula)
	assocparams = param.AssociatedParameters
	associatedparams.append(assocparams)
	assocelems = list()
	for assoc in assocparams:
		assocelems.append(assoc.Element)
	associatedelements.append(assocelems)
	canassignformula.append(param.CanAssignFormula)
	
OUT = (pname,guid,pgroup,ptype,utype,dutype,stype,isinstance,isreporting,isshared,isreadonly,usermodifiable,formula,determinedbyformula,associatedparams,canassignformula,associatedelements)

##### NEXT PYTHON NODE #####

import clr
OUT = []
for chunks in IN[0]:
	sublist = []
	if chunks: [sublist.append(x) for x in chunks if x in IN[1]]
	OUT.append(sublist)
	