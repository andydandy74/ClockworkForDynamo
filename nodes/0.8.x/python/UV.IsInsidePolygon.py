import clr

# script found here:
# http://www.ariel.com.au/a/python-point-int-poly.html
# (with sight alterations for booleans)

def point_inside_polygon(x,y,poly):
    n = len(poly)
    inside = 0
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = 1 - inside
        p1x,p1y = p2x,p2y
    if inside == 1: return True
    else: return False
    
poly = IN[0]
points = IN[1]
elementlist = list()
for point in points:
	elementlist.append(point_inside_polygon(point[0],point[1],poly))
OUT = elementlist