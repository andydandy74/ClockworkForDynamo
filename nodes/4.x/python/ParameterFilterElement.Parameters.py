import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
bips = {}
for bip in [eval("BuiltInParameter."+x) for x in dir(BuiltInParameter) if not any(y.islower() for y in x)]:
    try: bips[ElementId(bip).Value] = LabelUtils.GetLabelFor(bip)
    except: pass
        
def GetFilterRuleParams(efilter, doc):
    params = []
    if efilter:
        for filter in efilter.GetFilters():
            if hasattr(filter, "GetRules"):
                for rule in filter.GetRules():
                    paramId = rule.GetRuleParameter()
                    thisparam = doc.GetElement(paramId)
                    if thisparam: thisparam = thisparam.Name
                    elif paramId != ElementId.InvalidElementId: thisparam = bips[paramId.Value]
                    params.append(thisparam.strip())
            else: params.append(GetFilterRuleParams(filter, doc))
    return params

if isinstance(IN[0], list): OUT = [GetFilterRuleParams(x.GetElementFilter(), x.Document) for x in items]
else: OUT = GetFilterRuleParams(items.GetElementFilter(), items.Document)