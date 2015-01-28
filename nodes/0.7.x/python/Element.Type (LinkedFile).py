import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
doc = UnwrapElement(IN[1])
typelist = list()
for item in items:
	try: 
		typelist.append(doc.GetElement(item.GetTypeId()))
	except:
		typelist.append(list())
OUT = typelist