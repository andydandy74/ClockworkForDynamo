import clr
from System.Collections.Generic import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
if isinstance(IN[1], list): xyz = [UnwrapElement(x).ToXyz() for x in IN[1]]
else: xyz = UnwrapElement(IN[1]).ToXyz()
rehost = IN[2]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): 
	if isinstance(IN[1], list):
		itemlist = [List[ElementId]([x.Id]) for x in items]
		if rehost: 
			newitems2 = [ElementTransformUtils.CopyElements(doc,x,doc,Transform.CreateTranslation(y),None) for x, y in zip(itemlist,xyz)]
			newitems = [x[0] for x in newitems2]
		else:
			newitems2 = [ElementTransformUtils.CopyElements(doc,x,y) for x, y in zip(itemlist,xyz)]
			newitems = [x[0] for x in newitems2]
	else:
		ids = [x.Id for x in items]
		itemlist = List[ElementId](ids)
		if rehost: newitems = ElementTransformUtils.CopyElements(doc,itemlist,doc,Transform.CreateTranslation(xyz),None)
		else: newitems = ElementTransformUtils.CopyElements(doc,itemlist,xyz)
else:
	if isinstance(IN[1], list):
		itemlist1 = List[ElementId]([items.Id]) 
		itemlist = []
		[itemlist.append(itemlist1) for x in xyz]
		if rehost: 
			newitems2 = [ElementTransformUtils.CopyElements(doc,x,doc,Transform.CreateTranslation(y),None) for x, y in zip(itemlist,xyz)]
			newitems = [x[0] for x in newitems2]
		else:
			newitems2 = [ElementTransformUtils.CopyElements(doc,x,y) for x, y in zip(itemlist,xyz)]
			newitems = [x[0] for x in newitems2]
	else:
		itemlist = List[ElementId]([items.Id])
		if rehost: newitems = ElementTransformUtils.CopyElements(doc,itemlist,doc,Transform.CreateTranslation(xyz),None)
		else: newitems = ElementTransformUtils.CopyElements(doc,itemlist,xyz)
TransactionManager.Instance.TransactionTaskDone()

if isinstance(IN[0], list) or isinstance(IN[1], list): OUT = [doc.GetElement(x).ToDSType(False) for x in newitems]
else: OUT = doc.GetElement(newitems[0]).ToDSType(False)