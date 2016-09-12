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
cstype = UnwrapElement(IN[0])
facerefs = IN[1]
elementlist = list()
refarr = ReferenceArray()
for ref in facerefs:
	refarr.Append(ref)
TransactionManager.Instance.EnsureInTransaction(doc)
doccreation = doc.Create
newcs = doccreation.NewCurtainSystem2(refarr,cstype)
try:
	newcs = doccreation.NewCurtainSystem2(refarr,cstype)
	for item in newcs:
		elementlist.append(doc.GetElement(item))
except:
	pass
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist