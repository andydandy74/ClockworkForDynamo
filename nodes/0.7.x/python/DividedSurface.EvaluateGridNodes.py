import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

ds = UnwrapElement(IN[0])
overhanging = IN[1]
uvlist = list()
uvnormals = list()
uvxyzs = list()

face = ds.Host.GetGeometryObjectFromReference(ds.HostReference)
gn = GridNode()
if overhanging == True:
	i = 0
	j = 1
else:
	i = 1
	j = 3
u = i
while (u < (ds.NumberOfUGridlines-i)):
	gn.UIndex = u
	v = i
	vlist = list()
	vnormals = list()
	vxyzs = list()
	while (v < (ds.NumberOfVGridlines-i)):
		gn.VIndex = v
		uv = ds.GetGridNodeUV(gn)
 		vlist.append(uv)
 		vnormals.append(face.ComputeNormal(uv).ToVector())
 		vxyzs.append(face.Evaluate(uv).ToPoint())
 		v += 1
 	uvlist.append(vlist)
 	uvnormals.append(vnormals)
 	uvxyzs.append(vxyzs)
 	u += 1
OUT = (uvnormals,uvxyzs,face.ToProtoType(),uvlist)