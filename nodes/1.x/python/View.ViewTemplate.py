import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
views = UnwrapElement(IN[0])
elementlist = list()

for view in views:
	if view.ViewTemplateId.IntegerValue == -1:
		elementlist.append(None)
	else:
		elementlist.append(view.Document.GetElement(view.ViewTemplateId))
OUT = elementlist