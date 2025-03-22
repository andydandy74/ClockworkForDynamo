import clr
import System.IO
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetName(item):
    unwrapped = UnwrapElement(item)
    try: utype = unwrapped.GetType().ToString()
    except: utype = ""
    if not unwrapped: return None
    elif utype in ("Autodesk.Revit.DB.Area", "Autodesk.Revit.DB.Architecture.TopographySurface"):
        try: return unwrapped.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
        except: return item.Name
    elif utype in ("Autodesk.Revit.DB.BuiltInParameter", "Autodesk.Revit.DB.BuiltInParameterGroup", "Autodesk.Revit.DB.DisplayUnitType", "Autodesk.Revit.DB.ParameterType", "Autodesk.Revit.DB.UnitSymbolType", "Autodesk.Revit.DB.UnitType"): 
        try: return LabelUtils.GetLabelFor(unwrapped)
        except: return unwrapped.ToString()
    elif utype in ("Autodesk.Revit.DB.Parameter", "Autodesk.Revit.DB.FamilyParameter"): return unwrapped.Definition.Name
    elif utype == "Revit.Application.Document": 
        if unwrapped.FilePath: return System.IO.Path.GetFileName(unwrapped.FilePath)
        else: return None
    elif utype == ("Autodesk.Revit.DB.ForgeTypeId"): 
        try: return LabelUtils.GetLabelForSpec(unwrapped)
        except: 
            try: return LabelUtils.GetLabelForSymbol(unwrapped)
            except: 
                try: return LabelUtils.GetLabelForUnit(unwrapped)
                except: 
                    try: return LabelUtils.GetLabelForGroup(unwrapped)
                    except: 
                        try: return LabelUtils.GetLabelForBuiltinParameter(unwrapped)
                        except: 
                            try: return LabelUtils.GetLabelForDiscipline(unwrapped)
                            except: return unwrapped.TypeId            
    elif hasattr(unwrapped, "GetName"): return unwrapped.GetName()  
    elif hasattr(item, "Name"): return item.Name
    elif hasattr(unwrapped, "Name"): return unwrapped.Name     
    else: return None

items = IN[0]
if isinstance(IN[0], list): OUT = [GetName(x) for x in IN[0]]
else: OUT = GetName(IN[0])