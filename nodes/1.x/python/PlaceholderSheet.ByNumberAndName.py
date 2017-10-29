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
sheetnums = IN[0]
sheetnames = IN[1]
elementlist = list()
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
for num in sheetnums:
	try:
		newsheet = ViewSheet.CreatePlaceholder(doc)
		newsheet.SheetNumber = num
		newsheet.Name = sheetnames[counter]
		elementlist.append(newsheet.ToDSType(False))
	except:
		elementlist.append(None)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist