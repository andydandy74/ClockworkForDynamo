# Based on https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f#gistcomment-3070256

dirs = []
dirs.append(['N', 'E', 'S', 'W'])
dirs.append(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
dirs.append(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])

def GetCardinalDirection(angle):
	if angle:
		ix = round(angle / (360. / len(cdirs)))
		return cdirs[int(ix % len(cdirs))]
	elif angle == 0: return 'N'
	else: return None

if IN[1] not in (0, 1, 2): IN[1] = 0
cdirs = dirs[IN[1]]
if isinstance(IN[0], list): OUT = [GetCardinalDirection(x) for x in IN[0]]
else: OUT = GetCardinalDirection(IN[0])