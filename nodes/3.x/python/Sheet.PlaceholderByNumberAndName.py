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

def MakePlaceholderSheet(num, name):
	try:
		newsheet = ViewSheet.CreatePlaceholder(doc)
		newsheet.SheetNumber = num
		newsheet.Name = name
		return newsheet.ToDSType(False)
	except:
		return None

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [MakePlaceholderSheet(x,y) for x,y in zip(sheetnums, sheetnames)]
	else: OUT = MakePlaceholderSheet(sheetnums[0],sheetnames)
else:
	if isinstance(IN[1], list): OUT = MakePlaceholderSheet(sheetnums,sheetnames[0])
	else: OUT = MakePlaceholderSheet(sheetnums,sheetnames)
TransactionManager.Instance.TransactionTaskDone()