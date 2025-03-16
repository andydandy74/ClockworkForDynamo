import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def MakeNewGroup(items, name):
    ids = []
    rejects = []
    for item in items:
        if item.Document.GetElement(item.GroupId): rejects.append(item)
        else:
            try: ids.append(item.Id)
            except: rejects.append(item)
    itemsNew = List[ElementId](ids)
    try:
        group = doc.Create.NewGroup(itemsNew)
        group.GroupType.Name = name
    except: 
        group = None
        rejects = items
    return group, rejects

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
names = IN[1]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[1], list):
    if isinstance(IN[0], list): OUT = list(zip(*[MakeNewGroup(x, y) for x, y in zip (items, names)]))
    else: OUT = MakeNewGroup(items, names[0])
else: OUT = MakeNewGroup(items, names)
TransactionManager.Instance.TransactionTaskDone()