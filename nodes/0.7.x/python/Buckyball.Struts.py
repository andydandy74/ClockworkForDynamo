import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

points = IN[0]
almostzero = IN[1]
struts = list()

# this function recursively finds all the pairs of points of the buckyball struts
def BuckyballStruts(points,struts):
	firstpoint = points[0]
	restofpoints = points[1:]
	# measure distance between first point and rest of points
	distances = [firstpoint.DistanceTo(x) for x in restofpoints]
	# filter out all points that do not have a distance of 2 to the first point
	strutpoints = list()
	strutpointpairs = list()
	i = 0
	for dist in distances:
		# use a little tolerance so we catch all struts
		if dist > 2 - almostzero and dist < 2 + almostzero:
			strutpoints.append(restofpoints[i])
			strutpointpairs.append((firstpoint,restofpoints[i]))
		i += 1
	# add strutpointpairs to struts
	if len(strutpointpairs) > 0: struts.extend(strutpointpairs)
	# Continue processing the list recursively until there's only one point left. By always removing the first point from the list, we ensure that no duplicate struts are computed.
	if len(restofpoints) > 1:
		return BuckyballStruts(restofpoints,struts)
	else: return (restofpoints,struts)
	
OUT = BuckyballStruts(points,struts)[1]