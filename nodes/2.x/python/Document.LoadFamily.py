import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
fampaths = IN[0]
famnames = IN[1]
elementlist = []
booleans = []

TransactionManager.Instance.EnsureInTransaction(doc)
for fampath in fampaths:
	try: 
		doc.LoadFamily(fampath)
		booleans.append(True)
	except: booleans.append(False)
TransactionManager.Instance.TransactionTaskDone()

collector = FilteredElementCollector(doc)
collector.OfClass(Family)
for item in collector.ToElements():
	if item.Name in famnames:
		typelist = list()
		for famtypeid in item.GetFamilySymbolIds():
			typelist.append(doc.GetElement(famtypeid).ToDSType(True))
		elementlist.append(typelist)
OUT = (elementlist,booleans)