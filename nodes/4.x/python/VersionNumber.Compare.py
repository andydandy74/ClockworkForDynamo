import sys
import clr
from System import Version

if isinstance(IN[0], list): 
	if isinstance(IN[1], list): OUT = [Version(x).CompareTo(Version(y)) for x,y in zip(IN[0], IN[1])]
	else: OUT = [Version(x).CompareTo(Version(IN[1])) for x in IN[0]]
else: 
	if isinstance(IN[1], list): OUT = [Version(IN[0]).CompareTo(Version(x)) for x in IN[1]]
	else: OUT = Version(IN[0]).CompareTo(Version(IN[1]))