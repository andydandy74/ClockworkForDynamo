import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

grouptypes = UnwrapElement(IN[0])

def GroupTypeInstances(gt):
	if gt.GetType().ToString() == "Autodesk.Revit.DB.GroupType":
		return [x.ToDSType(True) for x in gt.Groups]
	else: return []

if isinstance(IN[0], list): OUT = [GroupTypeInstances(x) for x in grouptypes]
else: OUT = GroupTypeInstances(grouptypes)