import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetAllInstances(item):
	collector = FilteredElementCollector(item.Document)
	bic = System.Enum.ToObject(BuiltInCategory, item.Category.Id.IntegerValue)
	collector.OfCategory(bic)
	# This is a workaround
	# because I was too lazy to learn
	# how to implement LINQ in Python
	return [x for x in collector.ToElements() if x.GetTypeId().IntegerValue == item.GetTypeId().IntegerValue]

elements = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetAllInstances(x) for x in elements]
else: OUT = GetAllInstances(elements)