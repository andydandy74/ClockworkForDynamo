import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def AssociateWithGlobalParam(item, param, gparam):
    rparams = item.GetParameters(param)
    if len(rparams) > 0: 
        try: 
            rparams[0].AssociateWithGlobalParameter(ElementId(gparam.Id))
            return True
        except: return False
    else: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
param = IN[1]
gparam = IN[2]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [AssociateWithGlobalParam(x, param, gparam) for x in items]
else: OUT = AssociateWithGlobalParam(items, param, gparam)
TransactionManager.Instance.TransactionTaskDone()