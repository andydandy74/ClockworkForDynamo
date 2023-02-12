import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def IsLinked(item):
	if item.GetType().ToString() == "Autodesk.Revit.DB.ImportInstance":
		if item.IsLinked: return True
		else: return False
	else: return False

doc = DocumentManager.Instance.CurrentDBDocument
impinst = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = [IsLinked(x) for x in impinst]
else: OUT = IsLinked(impinst)