import clr

# based on a script found here:
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python

points = IN[0]
#reformat points list
newpoints = list()
for pair in points:
	newpoint = (pair[0],pair[1])
	newpoints.append(newpoint)
points = sorted(set(newpoints))

def cross(o, a, b):
	return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
 
if len(points) <= 1:
	OUT = points
else:
	lower = []
	for p in points:
		while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
			lower.pop()
		lower.append(p)
	upper = []
	for p in reversed(points):
		while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
			upper.pop()
		upper.append(p)
	OUT = lower[:-1] + upper[:-1]