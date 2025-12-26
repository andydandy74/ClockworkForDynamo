import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstancesAtLevel(item, lvl):
    collector = FilteredElementCollector(item.Document)
    catID = item.Category.Id.Value
    bic = System.Enum.ToObject(BuiltInCategory, catID)
    lvlfilter = ElementLevelFilter(lvl.Id)
    collector.OfCategory(bic).WherePasses(lvlfilter)
    return [x for x in collector.ToElements() if x.GetTypeId().Value == item.GetTypeId().Value]

elements = UnwrapElement(IN[0])
lvl = UnwrapElement(IN[1])

if isinstance(IN[0], list): OUT = [GetAllInstancesAtLevel(x, lvl) for x in elements]
else: OUT = GetAllInstancesAtLevel(elements, lvl)