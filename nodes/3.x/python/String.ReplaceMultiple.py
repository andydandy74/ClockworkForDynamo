# Based on https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729

import clr
import re

def ReplaceMultiple(str, searchstr, replacestr, sort):
	replacements = dict(zip(searchstr, replacestr))
	if sort: substrs = sorted(replacements, key=len, reverse=True)
	else: substrs = searchstr
	regexp = re.compile('|'.join(map(re.escape, substrs)))
	return regexp.sub(lambda match: replacements[match.group(0)], str)
	
if isinstance(IN[1], list): searchstr = IN[1]
else: searchstr = [IN[1]]
if isinstance(IN[2], list): replacestr = IN[2]
else: replacestr = [IN[2]]

if isinstance(IN[0], list): OUT = [ReplaceMultiple(x, searchstr, replacestr, IN[3]) for x in IN[0]]
else: OUT = ReplaceMultiple(IN[0], searchstr, replacestr, IN[3])