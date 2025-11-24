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

def DissociateFromGlobalParam(item, param):
    rparams = item.GetParameters(param)
    if len(rparams) > 0: 
        try: 
            rparams[0].DissociateFromGlobalParameter()
            return True
        except: return False
    else: return False

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
param = IN[1]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [DissociateFromGlobalParam(x, param) for x in items]
else: OUT = DissociateFromGlobalParam(items, param)
TransactionManager.Instance.TransactionTaskDone()