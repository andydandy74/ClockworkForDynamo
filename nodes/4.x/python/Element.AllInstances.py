import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstances(item):
    collector = FilteredElementCollector(item.Document)
    catID = item.Category.Id.Value
    bic = System.Enum.ToObject(BuiltInCategory, catID)
    collector.OfCategory(bic)
    return [x for x in collector.ToElements() if x.GetTypeId().Value == item.GetTypeId().Value]

elements = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetAllInstances(x) for x in elements]
else: OUT = GetAllInstances(elements)