import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

famtypes = UnwrapElement(IN[0])
elementlist = list()
for item in famtypes:
	try: 
		elementlist.append(item.FamilyName)
	except:
		elementlist.append(None)
			
OUT = elementlist