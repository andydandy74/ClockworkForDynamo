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

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
    sourcelist = list()
    for source in item.GetSourceElementIds():
        sourcelist.append(doc.GetElement(source.HostElementId).ToDSType(True))
    if len(sourcelist) < 2:
        elementlist.append(sourcelist[0])
    else:
        elementlist.append(sourcelist)
OUT = elementlist