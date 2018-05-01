import clr
import re

if isinstance(IN[1], list): OUT = [IN[0].sub(IN[2],x) for x in IN[1]]
else: OUT = IN[0].sub(IN[2],IN[1])
