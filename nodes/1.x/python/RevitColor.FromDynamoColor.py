import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
appcreation = Creation.Application
r = IN[0]
g = IN[1]
b = IN[2]
counter = 0
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for red in r:
	try:
		newcolor = Color(red,g[counter],b[counter])
		elementlist.append(newcolor)
	except:
		elementlist.append(None)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist