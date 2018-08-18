import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
typelist = list()
for item in items:
	try: 
		typelist.append(item.Document.GetElement(item.GetTypeId()))
	except:
		typelist.append(None)
OUT = typelist