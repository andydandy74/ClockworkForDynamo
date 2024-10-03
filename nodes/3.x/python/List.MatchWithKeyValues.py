import clr

items = IN[0]
keys = IN[1]
values = IN[2]
elementlist = list()
for item in items:
	counter = 0
	hasmatch = False
	for key in keys:
		if (item == key):
			elementlist.append(values[counter])
			hasmatch = True
		counter += 1
	if hasmatch == False:
		elementlist.append(None)
OUT = elementlist