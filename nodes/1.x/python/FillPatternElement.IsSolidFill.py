import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fillpatterns = UnwrapElement(IN[0])
booleans = list()

for fp in fillpatterns:
	booleans.append(fp.GetFillPattern().IsSolidFill)
OUT = booleans