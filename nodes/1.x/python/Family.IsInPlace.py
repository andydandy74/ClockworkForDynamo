import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fams = UnwrapElement(IN[0])
elementlist = list()

for fam in fams:
	if fam.GetType().ToString() == "Autodesk.Revit.DB.Family":
		elementlist.append(fam.IsInPlace)
	else: elementlist.append(False)
OUT = elementlist