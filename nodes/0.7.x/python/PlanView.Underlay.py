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
	try:
		if view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId().IntegerValue == -1:
			elementlist.append(list())
		else:
			elementlist.append(doc.GetElement(view.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID).AsElementId()))
	except:
		elementlist.append(list())
OUT = elementlist