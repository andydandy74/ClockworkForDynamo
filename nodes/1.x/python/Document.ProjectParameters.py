import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

inputdoc = UnwrapElement(IN[1])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

names = []
cats = []
vag = []
iterator = doc.ParameterBindings.ForwardIterator()
while iterator.MoveNext():
	vag.append(iterator.Key.VariesAcrossGroups)
	names.append(iterator.Key.Name)
	thesecats = []
	for cat in iterator.Current.Categories:
		try:
			thesecats.append(Revit.Elements.Category.ById(cat.Id.IntegerValue))
		except:
			# Return null if category is not supported by Dynamo
			# This way the user knows there are unsupported categories assigned
			thesecats.append(None)
	cats.append(thesecats)
OUT = (names,cats,vag)