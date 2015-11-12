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
	try:
		elementlist.append(str(workset.Kind))
	except:
		elementlist.append(list())
OUT = elementlist