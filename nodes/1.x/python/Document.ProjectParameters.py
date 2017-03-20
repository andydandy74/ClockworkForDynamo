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

doc = DocumentManager.Instance.CurrentDBDocument
params = []
cats = []
iterator = doc.ParameterBindings.ForwardIterator()
while iterator.MoveNext():
	params.append(iterator.Key.Name)
	thesecats = []
	for cat in iterator.Current.Categories:
		thesecats.append(Revit.Elements.Category.ById(cat.Id.IntegerValue))
	cats.append(thesecats)
OUT = (params,cats)