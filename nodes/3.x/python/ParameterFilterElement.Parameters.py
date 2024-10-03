import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

bips = {}
for bip in System.Enum.GetValues(BuiltInParameter):
	try: bips[ElementId(bip).IntegerValue] = LabelUtils.GetLabelFor(bip)
	except: pass

def GetFilterRuleParamsWrapper(item):
	if version > 2018 and hasattr(item, "GetElementFilter"): 
		efilter = item.GetElementFilter()
		return GetFilterRuleParams(efilter, item.Document)		
	elif version < 2019 and hasattr(item, "GetRules"): 
		return "Versions below Revit 2019 not supported"
		
def GetFilterRuleParams(efilter, doc):
	params = []
	if efilter:
		for filter in efilter.GetFilters():
			if hasattr(filter, "GetRules"):
				for rule in filter.GetRules():
					paramId = rule.GetRuleParameter()
					thisparam = doc.GetElement(paramId)
					if thisparam: thisparam = thisparam.Name
					else: thisparam = bips[paramId.IntegerValue]
					params.append(thisparam.strip())
			else: params.append(GetFilterRuleParams(filter, doc))
	return params
		
items = UnwrapElement(IN[0])
version = IN[1]

if isinstance(IN[0], list): OUT = [GetFilterRuleParamsWrapper(x) for x in items]
else: OUT = GetFilterRuleParamsWrapper(items)