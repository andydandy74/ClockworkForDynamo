import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
faminsts = UnwrapElement(IN[0])
elementlist = list()
for item in faminsts:
	try:
		elementlist.append(doc.GetWorksetTable().GetWorkset(item.WorksetId))
	except:
		elementlist.append(None)
OUT = elementlist