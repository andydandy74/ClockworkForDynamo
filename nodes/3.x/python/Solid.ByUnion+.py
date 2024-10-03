import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

solids = IN[0]
OUT = [solids[0]]
solids = solids[1:]

for s in solids:
	i = 0
	unionDone = False
	while i < len(OUT):
		try:
			OUT[i] = OUT[i].Union(s)
			unionDone = True
			break
		except:	i += 1
	if not unionDone: OUT.append(s)