import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
red = IN[0]
green = IN[1]
blue = IN[2]

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): OUT = [Color(r, g, b) for r, g, b in zip(red, green, blue)]
else: OUT = Color(red, green, blue)
TransactionManager.Instance.TransactionTaskDone()