import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import os

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
path = IN[0]
compact = IN[1]
newcentral = IN[2]
isworkshared = IN[3]
astemplate = IN[4]

TransactionManager.Instance.ForceCloseTransaction()
if doc.IsFamilyDocument:
	path += '.rfa'
else:
	if astemplate: path += '.rte'
	else: path += '.rvt'
opt = SaveAsOptions()
opt.OverwriteExistingFile = True
opt.Compact = compact
if isworkshared and newcentral and not astemplate:
	wsopt = WorksharingSaveAsOptions()
	wsopt.ClearTransmitted = True
	wsopt.SaveAsCentral = True
	opt.SetWorksharingOptions(wsopt)
try:
	doc.SaveAs(path, opt)
	if doc.IsFamilyDocument and astemplate: 
		newpath = path.replace(".rfa", ".rft")
		os.rename(path, newpath)
	OUT = True
except:
	try:
		wsopt.ClearTransmitted = False
		opt.SetWorksharingOptions(wsopt)
		doc.SaveAs(path, opt)
		OUT = True
	except:
		OUT = False