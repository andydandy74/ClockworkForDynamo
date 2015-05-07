import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
elements = UnwrapElement(IN[0])
selection = UnwrapElement(IN[1])

elementlist = list()
for e in elements:
	elist =  list()
	for item in selection:
		if item.GetTypeId().IntegerValue == e.GetTypeId().IntegerValue:
			elist.append(item)
	elementlist.append(elist)
OUT = elementlist