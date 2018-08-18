import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
impinst = UnwrapElement(IN[0])
booleans = []
for item in impinst:
	if item.GetType().ToString() == "Autodesk.Revit.DB.ImportInstance":
		if item.IsLinked: booleans.append(True)
		else: booleans.append(False)
	else: booleans.append(False)
OUT = (booleans)