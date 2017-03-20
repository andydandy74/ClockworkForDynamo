import clr
import re

thisexp = IN[0]
regexlist = IN[1]
replacement = IN[2]
elementlist = list()
for item in regexlist:
	try:
		elementlist.append(thisexp.sub(replacement,item))
	except:
		elementlist.append(list())
OUT = elementlist