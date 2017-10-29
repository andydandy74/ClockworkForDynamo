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
			fromlist.append(None)
		if item.ToRoom[phase]:
			tolist.append(item.ToRoom[phase])
			exits += 1
		else:
			tolist.append(None)
	except:
		fromlist.append(None)
		tolist.append(None)
	numexits.append(exits)
OUT = (fromlist,tolist,numexits)