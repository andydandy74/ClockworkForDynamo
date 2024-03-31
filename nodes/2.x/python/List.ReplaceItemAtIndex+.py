_list = IN[0]
rValues = IN[1]
iValues = IN[2]
if iValues:
	if isinstance(iValues, list):
		if not isinstance(rValues, list): rValues = [rValues] * len(iValues)
		for (index, value) in zip(iValues, rValues):
			_list[index] = value
	else: _list[iValues] = rValues
OUT = _list