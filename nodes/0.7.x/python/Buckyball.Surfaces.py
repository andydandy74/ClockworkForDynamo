import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

struts = IN[0]
points = IN[1]
almostzero = IN[2]

def BuckyballFaces(struts,points,planes,almostzero,vertices):
	firststrut = struts[0]
	struts.pop(0)
	# find the two adjacent struts
	adjacent = list()
	for strut in struts:
		for point in strut:
			if point.IsAlmostEqualTo(firststrut[0]):
				adjacent.append(strut)
				break
		if len(adjacent) == 2:
			break
	# identify planes and find all vertices on planes		
	vlist = list()		
	for item in adjacent:
		triangle = (firststrut[1],item[0],item[1])
		pl = Plane.ByBestFitThroughPoints(triangle)	
		vlist = list()
		for point in points:
			dist = pl.DistanceTo(point)
			if dist < almostzero and dist > -almostzero:
				vlist.append(point)
		newplane = (Plane.ByBestFitThroughPoints(vlist))
		append_vertices = True
		for pl in planes:
			if newplane.IsAlmostEqualTo(pl):
				append_vertices = False
		if append_vertices: 
			vertices.append(vlist)
			planes.append(newplane)
	# let this function recursively call itself until it finds all planes
	if len(planes) < 32:
		return BuckyballFaces(struts,points,planes,almostzero,vertices)
	else:
		return (struts,points,planes,almostzero,vertices)

def OrderFaceIndices(p_ordered,p_unordered,almostzero):
	i = 0;
	for p in p_unordered:
		dist = p_ordered[(len(p_ordered)-1)].DistanceTo(p)
		if dist > 2-almostzero and dist < 2+almostzero:
			p_ordered.append(p)
			p_unordered.pop(i)
			break
		i += 1
	if len(p_unordered) > 0:
		return OrderFaceIndices(p_ordered,p_unordered,almostzero)
	else:
		return (p_ordered,p_unordered,almostzero)

vlist_unordered = BuckyballFaces(struts,points,list(),almostzero,list())[4]

vset_ordered = list()
for vset in vlist_unordered:
	p_ordered = [vset[0]]
	vset.pop(0)
	vset_ordered.append(OrderFaceIndices(p_ordered,vset,almostzero))

vset_out = list()
for vset in vset_ordered:
	vset_out.append(vset[0])
OUT = vset_out