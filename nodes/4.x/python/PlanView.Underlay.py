import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import System

def GetUnderlays(view):
    baselvl = None
    toplvl = None
    ulOrientation = None
    if hasattr(view, "GetUnderlayBaseLevel"):    
        if view.GetUnderlayBaseLevel() != ElementId.InvalidElementId: baselvl = view.Document.GetElement(view.GetUnderlayBaseLevel())
        if view.GetUnderlayTopLevel() != ElementId.InvalidElementId: toplvl = view.Document.GetElement(view.GetUnderlayTopLevel())
        ulOrientation = System.Enum.GetName(UnderlayOrientation, view.GetUnderlayOrientation())
    return baselvl, toplvl, ulOrientation

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[GetUnderlays(x) for x in views]))
else: OUT = GetUnderlays(views)