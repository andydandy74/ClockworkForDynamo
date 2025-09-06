import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
version = IN[1]
bips = {}
for bip in [eval("BuiltInParameter."+x) for x in dir(BuiltInParameter) if not any(y.islower() for y in x)]:
    try: 
        if version > 2024: bips[ElementId(bip).Value] = LabelUtils.GetLabelFor(bip)
        else: bips[ElementId(bip).IntegerValue] = LabelUtils.GetLabelFor(bip)
    except: pass
        
def GetFilterRuleString(efilter, doc):
    rulestrings = []
    # Filters without rules will arrive as nulls:
    if not efilter: return '<<<No rules defined>>>'
    efilterstr = efilter.ToString()        
    if "And" in efilterstr: sep = " AND "
    elif "Or" in efilterstr: sep = " OR "
    else: sep = ""
    if hasattr(efilter, "GetFilters"): filters = efilter.GetFilters()
    else: filters = [efilter]
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
                elif paramId != ElementId.InvalidElementId: 
                    if version > 2024: thisparam = bips[paramId.Value]
                    else: thisparam = bips[paramId.IntegerValue]
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
                elif hasattr(rule, "RuleValue"): thisval = str(rule.RuleValue)
                else: thisval = ""
                if useRule: rulestrings.append((thisparam + " " + thiseval + " " + thisval).strip())
        else: rulestrings.append("(" + GetFilterRuleString(filter, doc)+ ")")
    rulestrings.sort()
    return sep.join(rulestrings)

if isinstance(IN[0], list): OUT = [GetFilterRuleString(x.GetElementFilter(), x.Document) for x in items]
else: OUT = GetFilterRuleString(items.GetElementFilter(), items.Document)
