import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk

bips = [eval("BuiltInParameter."+x) for x in dir(BuiltInParameter) if not any(y.islower() for y in x)]
pdata = list()
for bip in bips:
	try:
		pdata.append((System.Enum.GetName(BuiltInParameter, bip),ElementId(bip),LabelUtils.GetLabelFor(bip)))
	except:
		pass
OUT = pdata