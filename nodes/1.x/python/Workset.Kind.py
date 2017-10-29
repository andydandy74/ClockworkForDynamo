import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
worksets = UnwrapElement(IN[0])
elementlist = list()
for workset in worksets:
	if workset.GetType().ToString() == "Autodesk.Revit.DB.Workset":
		elementlist.append(str(workset.Kind))
	else: elementlist.append(None)
OUT = elementlist