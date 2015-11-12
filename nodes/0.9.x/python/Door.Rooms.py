import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
phase = UnwrapElement(IN[1])
fromlist = list()
tolist = list()
numexits = list()

for item in items:
	exits = 0
	try:	
		if item.FromRoom[phase]:
			fromlist.append(item.FromRoom[phase])
			exits += 1
		else:
			fromlist.append(list())
		if item.ToRoom[phase]:
			tolist.append(item.ToRoom[phase])
			exits += 1
		else:
			tolist.append(list())
	except:
		fromlist.append(list())
		tolist.append(list())
	numexits.append(exits)
OUT = (fromlist,tolist,numexits)