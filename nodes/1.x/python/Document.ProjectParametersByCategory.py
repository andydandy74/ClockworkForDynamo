import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

search_cats = UnwrapElement(IN[0])
search_ids = []
cats = []
for search_cat in search_cats:
	search_ids.append(search_cat.Id.IntegerValue)
	cats.append(list())
doc = DocumentManager.Instance.CurrentDBDocument
iterator = doc.ParameterBindings.ForwardIterator()
while iterator.MoveNext():
	for cat in iterator.Current.Categories:
		i = 0
		for search_id in search_ids:
			if cat.Id.IntegerValue == search_id:
				cats[i].append(iterator.Key.Name)
			i += 1
OUT = cats