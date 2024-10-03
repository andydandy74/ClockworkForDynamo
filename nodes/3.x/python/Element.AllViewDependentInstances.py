import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstancesInView(item, view):
	collector = FilteredElementCollector(item.Document)
	bic = System.Enum.ToObject(BuiltInCategory, item.Category.Id.IntegerValue)
	viewfilter = ElementOwnerViewFilter(view.Id)
	collector.WherePasses(viewfilter).OfCategory(bic)
	# This is a workaround
	# because I was too lazy to learn
	# how to implement LINQ in Python
	return [x for x in collector.ToElements() if x.GetTypeId().IntegerValue == item.GetTypeId().IntegerValue]

elements = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])

if isinstance(IN[0], list): OUT = [GetAllInstancesInView(x, view) for x in elements]
else: OUT = GetAllInstancesInView(elements, view)