import clr
import re

regexstring = IN[0]
regexlist = IN[1]
elementlist = list()
thisexp = re.compile(regexstring)
for item in regexlist:
	try:
		elementlist.append(thisexp.split(item))
	except:
		elementlist.append(list())
OUT = elementlist