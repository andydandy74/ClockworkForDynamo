import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

UVs = UnwrapElement(IN[0])
ulist = list()
vlist = list()
for uv in UVs:
	ulist.append(uv.U)
	vlist.append(uv.V)
OUT = (ulist,vlist)