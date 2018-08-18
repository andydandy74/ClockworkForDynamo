import clr

def isLater(date1, date2):
	return date1 > date2

dates1 = IN[0]
dates2 = IN[1]

if not dates1 or not dates2: OUT = None
elif isinstance(dates1, list) and isinstance(dates2, list): OUT = [isLater(x, y) for x,y in zip(dates1, dates2)]
elif isinstance(dates1, list): OUT = [isLater(x, dates2) for x in dates1]
elif isinstance(dates2, list): OUT = [isLater(dates1, x) for x in dates2]
else: OUT = isLater(dates1, dates2)