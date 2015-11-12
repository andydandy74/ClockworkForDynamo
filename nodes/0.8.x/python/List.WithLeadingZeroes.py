import clr

stringlist = IN[0]
stringlength = IN[1]
elementlist = list()
for item in stringlist:
	elementlist.append(item.zfill(stringlength))
OUT = elementlist