import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
phase = UnwrapElement(IN[1])
fromlist = list()
tolist = list()

for item in items:
	try:
		if item.FromRoom[phase]:
			fromlist.append(item.FromRoom[phase])
		else:
			fromlist.append(list())
		if item.ToRoom[phase]:
			tolist.append(item.ToRoom[phase])
		else:
			tolist.append(list())
	except:
		fromlist.append(list())
		tolist.append(list())
OUT = (fromlist,tolist)