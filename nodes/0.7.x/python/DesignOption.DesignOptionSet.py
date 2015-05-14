import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
desopts = UnwrapElement(IN[0])
elementlist = list()
for item in desopts:
	elementlist.append(doc.GetElement(item.get_Parameter(BuiltInParameter.OPTION_SET_ID).AsElementId()))
OUT = elementlist