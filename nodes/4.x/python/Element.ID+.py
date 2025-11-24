import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetId(item):
    if hasattr(item, "Id"): 
        if version > 2024: return item.Id.Value
        else: return item.Id.IntegerValue
    else: return None

items = UnwrapElement(IN[0])
version = IN[1]

if isinstance(IN[0], list): OUT = [GetId(x) for x in items]
else: OUT = GetId(items)