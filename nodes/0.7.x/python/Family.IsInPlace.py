import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fams = UnwrapElement(IN[0])
elementlist = list()

for fam in fams:
	try:
		elementlist.append(fam.IsInPlace)
	except:
		elementlist.append(False)
OUT = elementlist