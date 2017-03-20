import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

items = UnwrapElement(IN[0])
dlist = list()

for item in items:
	try:
		dlist.append(item.ViewDirection.ToVector())
	except:
		dlist.append(None)
OUT = dlist