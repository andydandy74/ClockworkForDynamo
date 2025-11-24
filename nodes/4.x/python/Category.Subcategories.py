import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetSubcategories(cat):
    if hasattr(cat, "SubCategories"):
        if version > 2025: return [Revit.Elements.Category.ById(x.Id.Value) for x in cat.SubCategories]
        else: return [Revit.Elements.Category.ById(x.Id.IntegerValue) for x in cat.SubCategories]
    else: return []

cats = UnwrapElement(IN[0])
version = IN[1]

if isinstance(IN[0], list): OUT = [GetSubcategories(x) for x in cats]
else: OUT = GetSubcategories(cats)