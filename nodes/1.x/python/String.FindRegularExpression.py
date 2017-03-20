import clr
import re

thisexp = IN[0]
regexlist = IN[1]
elementlist = list()
	
for item in regexlist:
	try:
		elementlist.append(thisexp.findall(item))
	except:
		elementlist.append(list())
OUT = elementlist