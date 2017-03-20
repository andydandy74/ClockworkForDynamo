import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])

elementlist = list()
unmatched = list()
for item in items:
	try: 
		elementlist.append(doc.GetElement(item).ToDSType(True))
	except:
		try:
			elementlist.append(doc.GetElement(ElementId(item)).ToDSType(True))
		except:
			unmatched.append(item)
OUT = (elementlist, unmatched)