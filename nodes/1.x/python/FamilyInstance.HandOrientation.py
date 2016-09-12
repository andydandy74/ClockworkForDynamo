import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

objinstances = UnwrapElement(IN[0])
vectorlist = list()
for item in objinstances:
	try:
		vectorlist.append(item.HandOrientation.ToVector())
	except:
		vectorlist.append(list())
OUT = vectorlist