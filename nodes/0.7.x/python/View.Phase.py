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
views = UnwrapElement(IN[0])
elementlist = list()
for view in views:
	elementlist.append(doc.GetElement(view.get_Parameter(BuiltInParameter.VIEW_PHASE).AsElementId()))
OUT = elementlist