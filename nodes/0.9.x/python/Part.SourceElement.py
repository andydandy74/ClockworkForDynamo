import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

items = UnwrapElement(IN[0])
elementlist = list()
for item in items:
    sourcelist = list()
    for source in item.GetSourceElementIds():
        sourcelist.append(item.Document.GetElement(source.HostElementId).ToDSType(True))
    if len(sourcelist) < 2:
        elementlist.append(sourcelist[0])
    else:
        elementlist.append(sourcelist)
OUT = elementlist