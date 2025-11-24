import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstancesAtLevel(item, lvl):
    collector = FilteredElementCollector(item.Document)
    if version > 2024: catID = item.Category.Id.Value
    else: catID = item.Category.Id.IntegerValue
    bic = System.Enum.ToObject(BuiltInCategory, catID)
    lvlfilter = ElementLevelFilter(lvl.Id)
    collector.OfCategory(bic).WherePasses(lvlfilter)
    # This is a workaround
    # because I was too lazy to learn
    # how to implement LINQ in Python
    if version > 2024: return [x for x in collector.ToElements() if x.GetTypeId().Value == item.GetTypeId().Value]
    else: return [x for x in collector.ToElements() if x.GetTypeId().IntegerValue == item.GetTypeId().IntegerValue]

elements = UnwrapElement(IN[0])
lvl = UnwrapElement(IN[1])
version = IN[2]

if isinstance(IN[0], list): OUT = [GetAllInstancesAtLevel(x, lvl) for x in elements]
else: OUT = GetAllInstancesAtLevel(elements, lvl)