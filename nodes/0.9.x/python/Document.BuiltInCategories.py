import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk

bics = System.Enum.GetValues(BuiltInCategory)
cdata = list()
for bic in bics:
	try:
		cdata.append((bic,ElementId(bic)))
	except:
		pass
OUT = cdata