import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elementlist = list()
booleans = list()
for item in items:
	try:
		elementlist.append(item.Id)
		booleans.append(True)
	except:
		elementlist.append(None)
		booleans.append(False)
OUT = (elementlist, booleans)