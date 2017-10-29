import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

designoptions = UnwrapElement(IN[0])
elementlist = list()

for opt in designoptions:
	try:
		elementlist.append(opt.IsPrimary)
	except:
		elementlist.append(False)
OUT = elementlist