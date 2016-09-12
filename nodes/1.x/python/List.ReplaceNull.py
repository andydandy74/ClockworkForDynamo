items = IN[0]
rep = IN[1]
elementlist = list()
for item in items:
	if item is None: 
		item = rep
	elementlist.append(item)
OUT = elementlist