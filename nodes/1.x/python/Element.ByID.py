import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def ElementById(item, doc):
	try: 
		return doc.GetElement(item).ToDSType(True)
	except:
		try:
			return doc.GetElement(ElementId(item)).ToDSType(True)
		except:
			return None

items = UnwrapElement(IN[0])
inputdoc = UnwrapElement(IN[1])
if not inputdoc: doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document": doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument

if isinstance(IN[0], list): OUT = [ElementById(x, doc) for x in items]
else: OUT = ElementById(items, doc)