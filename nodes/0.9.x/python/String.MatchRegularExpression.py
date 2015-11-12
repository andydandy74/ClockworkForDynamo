import clr
import re

regexstring = IN[0]
regexlist = IN[1]
elementlist = list()
thisexp = re.compile(regexstring)
for item in regexlist:
	if (str(thisexp.search(item)) == 'None'):
		elementlist.append(False)
	else:
		elementlist.append(True)
OUT = elementlist