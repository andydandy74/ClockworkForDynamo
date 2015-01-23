import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
elementlist = list()

for item in items:
	elementlist.append(dir(item))
OUT = elementlist