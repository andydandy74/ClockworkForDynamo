import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
import Autodesk
clr.AddReference("RevitNodes")
import Revit

bics = System.Enum.GetValues(BuiltInCategory)
cdata = list()
for bic in bics:
	try:
		cdata.append((bic,ElementId(bic),Revit.Elements.Category.ById(ElementId(bic).IntegerValue)))
	except:
		pass
OUT = cdata