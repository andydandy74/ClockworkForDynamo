import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetHostPanel(item):
    if hasattr(item, "FindHostPanel"):
        hpId = item.FindHostPanel()
        if version > 2024: hpIdVal = hpId.Value
        else: hpIdVal = hpId.IntegerValue
        if hpIdVal > 0: return item.Document.GetElement(hpId).ToDSType(True)
        else: return item
    else: return item

items = UnwrapElement(IN[0])
version = IN[1]

if isinstance(IN[0], list): OUT = [GetHostPanel(x) for x in items]
else: OUT = GetHostPanel(items)