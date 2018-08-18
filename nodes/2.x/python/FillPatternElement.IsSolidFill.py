import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsSolidFill(fp):
	return fp.GetFillPattern().IsSolidFill

fillpatterns = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [IsSolidFill(x) for x in fillpatterns]
else: OUT = IsSolidFill(fillpatterns)