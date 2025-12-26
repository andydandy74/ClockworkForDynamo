import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstancesInView(item, view):
    collector = FilteredElementCollector(item.Document)
    catID = item.Category.Id.Value
    bic = System.Enum.ToObject(BuiltInCategory, catID)
    viewfilter = ElementOwnerViewFilter(view.Id)
    collector.WherePasses(viewfilter).OfCategory(bic)
    return [x for x in collector.ToElements() if x.GetTypeId().Value == item.GetTypeId().Value]

elements = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])

if isinstance(IN[0], list): OUT = [GetAllInstancesInView(x, view) for x in elements]
else: OUT = GetAllInstancesInView(elements, view)