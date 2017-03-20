import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

scheds = UnwrapElement(IN[0])
elementlist = list()
for item in scheds:
	try:
		elementlist.append(item.KeyScheduleParameterName)
	except:
		elementlist.append(None)	
OUT = elementlist