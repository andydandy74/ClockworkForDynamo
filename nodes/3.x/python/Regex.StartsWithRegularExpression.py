import clr
import re

def StartsWithRegex(regex, str):
	if regex.match(str): return True
	else: return False

if isinstance(IN[1], list): OUT = [StartsWithRegex(IN[0], x) for x in IN[1]]
else: OUT = StartsWithRegex(IN[0], IN[1])