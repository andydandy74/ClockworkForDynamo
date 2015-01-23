import clr

inputlist = IN[0]
listlengths = IN[1]
rowcounter = 0
elementlist = list()
for item in listlengths:
	itemcounter = 0
	itemlist = list()
	while itemcounter < item:
		itemlist.append(inputlist[rowcounter])
		rowcounter += 1
		itemcounter += 1
	elementlist.append(itemlist)
OUT = elementlist