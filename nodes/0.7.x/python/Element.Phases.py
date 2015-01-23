import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
items = UnwrapElement(IN[0])
createdlist = list()
demolist = list()

for item in items:
	try:
		if item.CreatedPhaseId.IntegerValue == -1:
			createdlist.append(list())
		else:
			createdlist.append(doc.GetElement(item.CreatedPhaseId))
		if item.DemolishedPhaseId.IntegerValue == -1:
			demolist.append(list())
		else:
			demolist.append(doc.GetElement(item.DemolishedPhaseId))
	except:
		createdlist.append(list())
		demolist.append(list())
OUT = (createdlist,demolist)