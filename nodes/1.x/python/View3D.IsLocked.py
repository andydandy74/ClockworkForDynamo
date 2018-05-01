import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [x.IsLocked for x in views]
else: OUT = views.IsLocked