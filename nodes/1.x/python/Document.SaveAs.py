import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
path = IN[0]
compact = IN[1]
newcentral = IN[2]
isworkshared = IN[3]

TransactionManager.Instance.ForceCloseTransaction()
if doc.IsFamilyDocument:
	path += '.rfa'
else:
	path += '.rvt'
opt = SaveAsOptions()
opt.OverwriteExistingFile = True
opt.Compact = compact
if isworkshared and newcentral:
	wsopt = WorksharingSaveAsOptions()
	wsopt.ClearTransmitted = True
	wsopt.SaveAsCentral = True
	opt.SetWorksharingOptions(wsopt)
try:
	doc.SaveAs(path, opt)
	OUT = True
except:
	try:
		wsopt.ClearTransmitted = False
		opt.SetWorksharingOptions(wsopt)
		doc.SaveAs(path, opt)
		OUT = True
	except:
		OUT = False