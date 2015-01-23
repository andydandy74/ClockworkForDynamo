import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
elementlist = list()
olist = list()
dlist = list()

for item in items:
	try:
		olist.append(item.Origin.ToPoint())
		dlist.append(item.ViewDirection.ToVector())
	except:
		elementlist.append(list())
OUT = (olist,dlist)