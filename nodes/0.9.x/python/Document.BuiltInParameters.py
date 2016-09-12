import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk

bips = System.Enum.GetValues(BuiltInParameter)
pdata = list()
for bip in bips:
	try:
		pdata.append((bip,ElementId(bip),LabelUtils.GetLabelFor(bip)))
	except:
		pass
OUT = pdata