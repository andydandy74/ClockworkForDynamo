import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

fams = UnwrapElement(IN[0])
elementlist = list()

for fam in fams:
	try:
		copinglist = list()
		for id in fam.GetCopingIds():
			copinglist.append(fam.Document.GetElement(id))
		elementlist.append(copinglist)
	except:	elementlist.append(list())

OUT = elementlist