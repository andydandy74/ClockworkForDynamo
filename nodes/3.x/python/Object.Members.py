import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [dir(x) for x in items]
else: OUT = dir(items)