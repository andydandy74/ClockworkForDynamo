import clr
OUT = [x - y for x, y in zip(IN[0][1:], IN[0][:-1])], IN[0][-1]-IN[0][0]