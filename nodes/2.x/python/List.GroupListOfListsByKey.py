import clr
from itertools import groupby

items = IN[0]
groupindex = int(IN[1])
listlist = list()

for key, group in groupby(items, lambda x: x[groupindex]):
	elementlist = list()
	for thing in group:
		elementlist.append(thing)
	listlist.append(elementlist)
OUT = listlist