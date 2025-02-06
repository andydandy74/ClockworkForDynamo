import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk
clr.AddReference("RevitNodes")
import Revit

dynamoCatsOnly = IN[0]
biclist = [eval("BuiltInCategory."+x) for x in dir(BuiltInCategory) if x.startswith("OST_")]
cdata = []
for bic in biclist:
	try: cdata.append((System.Enum.GetName(BuiltInCategory, bic), ElementId(bic), Revit.Elements.Category.ById(ElementId(bic).IntegerValue)))
	except:
		if not dynamoCatsOnly: cdata.append((bic, ElementId(bic), None))
OUT = map(list, zip(*cdata))