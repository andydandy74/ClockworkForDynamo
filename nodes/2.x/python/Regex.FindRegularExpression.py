import clr
import re

if isinstance(IN[1], list): OUT = [IN[0].findall(x) for x in IN[1]]
else: OUT = IN[0].findall(IN[1])

"""
thisexp = IN[0]
regexlist = IN[1]
elementlist = list()
	
for item in regexlist:
	try:
		elementlist.append(thisexp.findall(item))
	except:
		elementlist.append(list())
OUT = elementlist"""