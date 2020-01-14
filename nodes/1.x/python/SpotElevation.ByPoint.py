import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])
pts = UnwrapElement(IN[1])
bend = UnwrapElement(IN[2])
end = UnwrapElement(IN[3])
leader = UnwrapElement(IN[4])
isoview = UnwrapElement(IN[5])
intsecvec = UnwrapElement(IN[6])
elementlist = []

i = 0;
TransactionManager.Instance.EnsureInTransaction(doc)
for pt in pts:
	view = views[i]
	pt = pt.ToXyz()
	refintsec = ReferenceIntersector(isoview)
	refintsec.TargetType = FindReferenceTarget.All
	try:
		ref = refintsec.FindNearest(pt,intsecvec[i].AsPoint().ToXyz()).GetReference()
		elementlist.append(doc.Create.NewSpotElevation(view, ref, pt, pt.Add(bend.AsPoint().ToXyz()), pt.Add(end.AsPoint().ToXyz()), pt, leader))
	except:
		elementlist.append(None)
	i += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist