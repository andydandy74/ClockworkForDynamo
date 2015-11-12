import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

textnotes = UnwrapElement(IN[0])
elementlist = list()
for item in textnotes:
	try:
		elementlist.append(item.Text)
	except:
		elementlist.append(list())
OUT = elementlist