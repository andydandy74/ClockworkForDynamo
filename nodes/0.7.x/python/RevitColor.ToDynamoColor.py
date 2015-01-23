import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

colors = UnwrapElement(IN[0])
rlist = list()
glist = list()
blist = list()

for color in colors:
	rlist.append(color.Red)
	glist.append(color.Green)
	blist.append(color.Blue)
OUT = (rlist,glist,blist)