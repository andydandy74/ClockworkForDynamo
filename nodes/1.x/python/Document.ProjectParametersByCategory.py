import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

search_cats = UnwrapElement(IN[0])
search_ids = []
names = []
vag = []
for search_cat in search_cats:
	search_ids.append(search_cat.Id.IntegerValue)
	names.append(list())
	vag.append(list())

inputdoc = UnwrapElement(IN[2])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

iterator = doc.ParameterBindings.ForwardIterator()
while iterator.MoveNext():
	for cat in iterator.Current.Categories:
		i = 0
		for search_id in search_ids:
			if cat.Id.IntegerValue == search_id:
				names[i].append(iterator.Key.Name)
				vag[i].append(iterator.Key.VariesAcrossGroups)
			i += 1
OUT = (names, vag)