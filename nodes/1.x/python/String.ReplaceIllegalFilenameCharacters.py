strings = IN[0]
replace = IN[1]
strlist = []
for str in strings:
	str = str.replace('/', replace)
	str = str.replace('?', replace)
	str = str.replace('<', replace)
	str = str.replace('>', replace)
	str = str.replace('\\', replace)
	str = str.replace(':', replace)
	str = str.replace('*', replace)
	str = str.replace('|', replace)
	str = str.replace('"', replace)
	str = str.replace('^', replace)
	strlist.append(str)
OUT = strlist