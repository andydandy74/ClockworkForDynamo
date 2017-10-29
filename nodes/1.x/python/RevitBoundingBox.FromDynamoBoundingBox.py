import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
minp = [x.ToXyz() for x in IN[0]]
maxp = [x.ToXyz() for x in IN[1]]
counter = 0
elementlist = list()
failedlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for newmin in minp:
	try:
		newbox = BoundingBoxXYZ()
		newbox.Max = maxp[counter]
		newbox.Min = newmin
		elementlist.append(newbox)
	except:
		elementlist.append(None)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist