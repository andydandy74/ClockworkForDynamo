import clr
from System import DateTime
OUT = [x.Subtract(y) for x, y in zip(IN[0][1:], IN[0][:-1])], IN[0][-1].Subtract(IN[0][0])