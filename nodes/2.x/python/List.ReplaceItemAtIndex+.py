_list = IN[0]
rValues = IN[1]
iValues = IN[2]
if len(iValues) > 1 and len(rValues) == 1:
	rValues = [rValues[0]] * len(iValues)
if len(iValues) > 0:
	for (index, value) in zip(iValues, rValues):
		_list[index] = value
OUT = _list