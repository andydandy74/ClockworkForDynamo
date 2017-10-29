import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

items = UnwrapElement(IN[0])
inputdoc = UnwrapElement(IN[1])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

elementlist = list()
for item in items:
	try: 
		elementlist.append(doc.GetElement(item).ToDSType(True))
	except:
		try:
			elementlist.append(doc.GetElement(ElementId(item)).ToDSType(True))
		except:
			elementlist.append(None)
OUT = elementlist