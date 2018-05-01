import clr
import re

if isinstance(IN[1], list): OUT = [IN[0].split(x) for x in IN[1]]
else: OUT = IN[0].split(IN[1])