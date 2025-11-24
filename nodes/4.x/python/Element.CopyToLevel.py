import clr
from System.Collections.Generic import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
source_views = UnwrapElement(IN[1])
target_views = UnwrapElement(IN[2])

def CopyToLevel(item, sview, tview):
	if item and sview and tview:
		itemlist = List[ElementId]([item.Id])
		results = ElementTransformUtils.CopyElements(sview,itemlist,tview, None, None)
		return doc.GetElement(results[0]).ToDSType(False)
	else: return None

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[2], list): OUT = [CopyToLevel(x,y,z) for x,y,z in zip(items, source_views, target_views)]
	else: OUT = [CopyToLevel(x,y,target_views) for x,y in zip(items, source_views)]
else:
	if isinstance(IN[2], list):
		multiitem = [items] * len(target_views)
		multisource = [source_views] * len(target_views)
		OUT = [CopyToLevel(x,y,z) for x,y,z in zip(multiitem, multisource, target_views)]
	else: OUT = CopyToLevel(items,source_views,target_views)
TransactionManager.Instance.TransactionTaskDone()