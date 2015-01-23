import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

footinginstances = UnwrapElement(IN[0])
elementlist = list()
for item in footinginstances:
	try:
		elementlist.append(item.FootingType.ToDSType(True))
	except:
		emptylist = list()
OUT = elementlist