import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

ds = UnwrapElement(IN[0])
overhanging = IN[1]
uvlist = []
uvnormals = []
uvxyzs = []

face = ds.Host.GetGeometryObjectFromReference(ds.HostReference)
               
if overhanging: i = 0     
else: i = 1
     
for u in range(i, ds.NumberOfUGridlines - i): 
    vlist = []
    vnormals = []
    vxyzs = []
    for v in range(i, ds.NumberOfVGridlines - i):
        # Construct GridNode with (u, v) directly
        gn = GridNode(u, v)
        uv = ds.GetGridNodeUV(gn)
        vlist.append(uv)
        vnormals.append(face.ComputeNormal(uv).ToVector())
        vxyzs.append(face.Evaluate(uv).ToPoint())
    uvlist.append(vlist)
    uvnormals.append(vnormals)
    uvxyzs.append(vxyzs)

OUT = (uvnormals, uvxyzs, face.ToProtoType(), uvlist)