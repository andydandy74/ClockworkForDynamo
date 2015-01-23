import clr

items = IN[0]
keys = IN[1]
values = IN[2]
elementlist = list()
for item in items:
	counter = 0
	for key in keys:
		if (item == key):
			elementlist.append(values[counter])
		counter += 1
OUT = elementlist