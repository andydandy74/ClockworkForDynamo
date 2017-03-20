import clr
import re

thisexp = IN[0]
regexlist = IN[1]
elementlist = list()
for item in regexlist:
	if (str(thisexp.search(item)) == 'None'):
		elementlist.append(False)
	else:
		elementlist.append(True)
OUT = elementlist