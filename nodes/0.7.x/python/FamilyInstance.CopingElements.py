import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
fams = UnwrapElement(IN[0])
elementlist = list()

for fam in fams:
	try:
		copinglist = list()
		for id in fam.GetCopingIds():
			copinglist.append(doc.GetElement(id))
		elementlist.append(copinglist)
	except:	elementlist.append(list())

OUT = elementlist