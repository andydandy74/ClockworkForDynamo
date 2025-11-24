import clr
import re

def ContainsRegex(regex, str):
	if regex.search(str): return True
	else: return False

if isinstance(IN[1], list): OUT = [ContainsRegex(IN[0], x) for x in IN[1]]
else: OUT = ContainsRegex(IN[0], IN[1])