import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

items = UnwrapElement(IN[0])
elementlist = []
for item in items:
	try:
		exref = ModelPathUtils.ConvertModelPathToUserVisiblePath(item.GetExternalFileReference().GetAbsolutePath())
		elementlist.append(exref)
	except:
		elementlist.append(list())
OUT = elementlist