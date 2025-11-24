import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from System.Collections.Generic import List

def SetElementType(item,itemtype):
    if hasattr(item, "ChangeTypeId"):
        try:
            itemcoll = List[ElementId]()
            itemcoll.Add(item.Id)
            Element.ChangeTypeId(item.Document, itemcoll, itemtype.Id)
            return True
        except: return False
    else: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
types = UnwrapElement(IN[1])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
    if isinstance(IN[1], list): OUT = [SetElementType(x,y) for x,y in zip(items,types)]
    else: OUT = [SetElementType(x,types) for x in items]
else:
    if isinstance(IN[1], list): OUT = SetElementType(items,types[0])
    else: OUT = SetElementType(items,types)
TransactionManager.Instance.TransactionTaskDone()