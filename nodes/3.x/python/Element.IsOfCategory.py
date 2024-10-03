cats = IN[0]
ecats = IN[1]
if isinstance(IN[1], list):
	if isinstance(IN[0], list):
		if len(cats) == len(ecats): OUT = [x == y for x, y in zip(cats, ecats)]
		else: OUT = [x in cats for x in ecats]
	else: OUT = [x == cats for x in ecats]
else:
	if isinstance(IN[0], list): OUT = ecats in cats
	else: OUT = cats == ecats