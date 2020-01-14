import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstancesAtLevel(item, lvl):
	collector = FilteredElementCollector(item.Document)
	bic = System.Enum.ToObject(BuiltInCategory, item.Category.Id.IntegerValue)
	lvlfilter = ElementLevelFilter(lvl.Id)
	collector.OfCategory(bic).WherePasses(lvlfilter)
	# This is a workaround
	# because I was too lazy to learn
	# how to implement LINQ in Python
	return [x for x in collector.ToElements() if x.GetTypeId().IntegerValue == item.GetTypeId().IntegerValue]

elements = UnwrapElement(IN[0])
lvl = UnwrapElement(IN[1])

if isinstance(IN[0], list): OUT = [GetAllInstancesAtLevel(x, lvl) for x in elements]
else: OUT = GetAllInstancesAtLevel(elements, lvl)