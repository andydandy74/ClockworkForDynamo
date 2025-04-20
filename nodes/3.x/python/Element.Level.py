import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetLevel(item):
    val = None
    if item:
        # some elements have an empty Category property
        try: 
            if version > 2024: catID = item.Category.Id.Value
            else: catID = item.Category.Id.IntegerValue
        except: catID = None
        # check all the different types of level properties...
        if hasattr(item, "LevelId"): 
            val = item.Document.GetElement(item.LevelId)
            if val: return val
        if hasattr(item, "Level"):
            val = item.Level
            if val: return val
        if hasattr(item, "GenLevel"):
            val = item.GenLevel
            if val: return val
        if (item.GetType().ToString() in ("Autodesk.Revit.DB.Architecture.StairsRun", "Autodesk.Revit.DB.Architecture.StairsLanding")):
            item = item.GetStairs()
        if (item.GetType().ToString() == "Autodesk.Revit.DB.Architecture.Stairs" or catID == int(BuiltInCategory.OST_Ramps)):
            try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.STAIRS_BASE_LEVEL_PARAM).AsElementId())
            except: pass
        if (item.GetType().ToString() == "Autodesk.Revit.DB.ExtrusionRoof"):
            try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.ROOF_CONSTRAINT_LEVEL_PARAM).AsElementId())
            except: pass
        if not val:
            try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_REFERENCE_LEVEL_PARAM).AsElementId())
            except: 
                try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM).AsElementId())
                except: 
                    try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM).AsElementId())
                    except: return None
        else: return None
    else: return None

items = UnwrapElement(IN[0])
version = IN[1]

if isinstance(IN[0], list): OUT = [GetLevel(x) for x in items]
else: OUT = GetLevel(items)