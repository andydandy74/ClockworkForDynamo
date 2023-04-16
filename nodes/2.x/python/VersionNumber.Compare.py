import sys
import clr
from System import Version

if isinstance(IN[0], list): 
	if isinstance(IN[1], list): OUT = [x.CompareTo(y) for x,y in zip(IN[0], IN[1])]
	else: OUT = [x.CompareTo(IN[1]) for x in IN[0]]
else: 
	if isinstance(IN[1], list): OUT = [IN[0].CompareTo(x) for x in IN[1]]
	else: OUT = IN[0].CompareTo(IN[1])