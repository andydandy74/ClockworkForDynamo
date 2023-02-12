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

def GetFilterRuleStringWrapper(item):
	if version > 2018 and hasattr(item, "GetElementFilter"): 
		return GetFilterRuleStringNew(item.GetElementFilter(), item.Document)		
	elif version < 2019 and hasattr(item, "GetRules"): 
		return GetFilterRuleStringOld(item)	
	else: return None
		
def GetFilterRuleStringOld(filter):
	rulestrings = []
	sep = " AND "
	doc = filter.Document
	if hasattr(filter, "GetRules"):
		for rule in filter.GetRules():
			# inverted rules
			ruleInverted = ""
			if hasattr(rule, "GetInnerRule"): 
				rule = rule.GetInnerRule()
				ruleInverted = "Not"
			# rule parameters
			paramId = filter.GetRuleParameter(rule)
			thisparam = doc.GetElement(paramId)
			if thisparam: thisparam = thisparam.Name
			else: thisparam = bips[paramId.IntegerValue]
			# rule evaluators
			if hasattr(rule, "GetEvaluator"):
				thiseval = rule.GetEvaluator().ToString().replace("Autodesk.Revit.DB.Filter","")
				thiseval = thiseval.replace("Numeric","")
				thiseval = thiseval.replace("String","")
				thiseval = thiseval + ruleInverted
				if thiseval == "Equals": thiseval = "=="
				elif thiseval == "EqualsNot": thiseval = "!="
				elif thiseval == "Greater": thiseval = ">"
				elif thiseval == "GreaterOrEqual": thiseval = ">="
				elif thiseval == "Less": thiseval = "<"
				elif thiseval == "LessOrEqual": thiseval = "<="
			elif hasattr(rule, "ParameterName"): thiseval = "Exists"
			else: thiseval = ""
			# rule values
			if hasattr(rule, "RuleString"): thisval = rule.RuleString
			elif hasattr(rule, "RuleValue"): thisval = rule.RuleValue.ToString()
			else: thisval = ""
			rulestrings.append((thisparam + " " + thiseval + " " + thisval).strip())
	if len(rulestrings) > 0:
		rulestrings.sort()
		return sep.join(rulestrings)
	else: return '<<<No rules defined>>>'
		
def GetFilterRuleStringNew(efilter, doc):
	rulestrings = []
	# Filters without rules will arrive as nulls:
	if not efilter: return '<<<No rules defined>>>'
	efilterstr = efilter.ToString()		
	if "And" in efilterstr: sep = " AND "
	elif "Or" in efilterstr: sep = " OR "
	else: sep = ""
	filters = efilter.GetFilters()
	for filter in filters:
		if hasattr(filter, "GetRules"):
			for rule in filter.GetRules():
				useRule = True
				# inverted rules
				ruleInverted = ""
				if hasattr(rule, "GetInnerRule"): 
					rule = rule.GetInnerRule()
					ruleInverted = "Not"
				# rule parameters
				paramId = rule.GetRuleParameter()
				thisparam = doc.GetElement(paramId)
				if thisparam: thisparam = thisparam.Name
				elif paramId.IntegerValue != -1: thisparam = bips[paramId.IntegerValue]
				# discard the rule if the parameter name cannot be resolved
				else: useRule = False
				# rule evaluators
				if hasattr(rule, "GetEvaluator"):
					thiseval = rule.GetEvaluator().ToString().replace("Autodesk.Revit.DB.Filter","")
					thiseval = thiseval.replace("Numeric","")
					thiseval = thiseval.replace("String","")
					thiseval = thiseval + ruleInverted
					if thiseval == "Equals": thiseval = "=="
					elif thiseval == "EqualsNot": thiseval = "!="
					elif thiseval == "Greater": thiseval = ">"
					elif thiseval == "GreaterOrEqual": thiseval = ">="
					elif thiseval == "Less": thiseval = "<"
					elif thiseval == "LessOrEqual": thiseval = "<="
				elif hasattr(rule, "ParameterName"): thiseval = "Exists"
				else: thiseval = ""
				# rule values
				if hasattr(rule, "RuleString"): thisval = rule.RuleString
				elif hasattr(rule, "RuleValue"): thisval = rule.RuleValue.ToString()
				else: thisval = ""
				if useRule: rulestrings.append((thisparam + " " + thiseval + " " + thisval).strip())
		else: rulestrings.append("(" + GetFilterRuleStringNew(filter, doc)+ ")")
	rulestrings.sort()
	return sep.join(rulestrings)
		
items = UnwrapElement(IN[0])
version = IN[1]

if isinstance(IN[0], list): OUT = [GetFilterRuleStringWrapper(x) for x in items]
else: OUT = GetFilterRuleStringWrapper(items)