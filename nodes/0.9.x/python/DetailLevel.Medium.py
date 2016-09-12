import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

OUT = ViewDetailLevel.Medium