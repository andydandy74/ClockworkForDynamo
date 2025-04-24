import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstancesInView(item, view):
    collector = FilteredElementCollector(item.Document)
    if version > 2024: catID = item.Category.Id.Value
    else: catID = item.Category.Id.IntegerValue
    bic = System.Enum.ToObject(BuiltInCategory, catID)
    viewfilter = ElementOwnerViewFilter(view.Id)
    collector.WherePasses(viewfilter).OfCategory(bic)
    # This is a workaround
    # because I was too lazy to learn
    # how to implement LINQ in Python
    if version > 2024: return [x for x in collector.ToElements() if x.GetTypeId().Value == item.GetTypeId().Value]
    else: return [x for x in collector.ToElements() if x.GetTypeId().IntegerValue == item.GetTypeId().IntegerValue]

elements = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])
version = IN[2]

if isinstance(IN[0], list): OUT = [GetAllInstancesInView(x, view) for x in elements]
else: OUT = GetAllInstancesInView(elements, view)