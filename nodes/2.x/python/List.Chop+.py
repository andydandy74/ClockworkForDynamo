import clr

def ListChopEvenly(l, n):
	# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
	return [l[i:i + n] for i in xrange(0, len(l), n)]

def ListChopUnevenly(l, n):
	count = 0
	max = len(l)
	chopped = []
	for num in n:
		if count + num > max: end = max
		else: end = count + num
		chopped.append(l[count:end])
		count = end	
	return chopped

if isinstance(IN[1], list): OUT = ListChopUnevenly(IN[0], IN[1])
else: OUT = ListChopEvenly(IN[0], IN[1])