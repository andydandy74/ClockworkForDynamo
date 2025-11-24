import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetAssociatedFamilyParameters(basearray):
    if basearray.GetType().ToString() in ("Autodesk.Revit.DB.LinearArray", "Autodesk.Revit.DB.RadialArray"):
        if basearray.Label != None: return basearray.Label, basearray.Label.Definition.Name
        else: return None, None
    else: return None, None

basearrays = UnwrapElement(IN[0])

if isinstance(IN[0], list): 
    if len(IN[0]) > 0: OUT = map(list, zip(*[GetAssociatedFamilyParameters(x) for x in basearrays]))
    else: OUT = [[],[]]
else: OUT = GetAssociatedFamilyParameters(basearrays)