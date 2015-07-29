_list = IN[0]
rValues = IN[1]
iValues = IN[2]
for (index, value) in zip(iValues, rValues):
	_list[index] = value
OUT = _list