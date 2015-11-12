import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
view = UnwrapElement(IN[1])
elementlist = list()
maxlist = list()
minlist = list()

for item in items:
	try:
		elementlist.append(item.BoundingBox[view])
		maxlist.append(item.BoundingBox[view].Max.ToPoint())
		minlist.append(item.BoundingBox[view].Min.ToPoint())
	except:
		donothing = 1
OUT = (elementlist,maxlist,minlist)