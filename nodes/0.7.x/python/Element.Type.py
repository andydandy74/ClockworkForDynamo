import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
typelist = list()
for item in items:
	try: 
		typelist.append(doc.GetElement(item.GetTypeId()))
	except:
		typelist.append(list())
OUT = typelist