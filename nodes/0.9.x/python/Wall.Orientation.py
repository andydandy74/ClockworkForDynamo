import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

wallinstances = UnwrapElement(IN[0])
vectorlist = list()
for item in wallinstances:
	try:
		vectorlist.append(item.Orientation.ToVector())
	except:
		vectorlist.append(list())
OUT = vectorlist