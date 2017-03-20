import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
path = IN[0]
compact = IN[1]
newcentral = IN[1]
isworkshared = IN[1]

if doc.IsFamilyDocument:
	path += '.rfa'
else:
	path += '.rvt'
opt = SaveAsOptions()
opt.OverwriteExistingFile = True
opt.Compact = compact
if isworkshared &amp; newcentral:
	wsopt = WorksharingSaveAsOptions()
	wsopt.ClearTransmitted = True
	wsopt.SaveAsCentral = True
	opt.SetWorksharingOptions(wsopt)
try:
	OUT = doc.SaveAs(path, opt)
except:
	wsopt.ClearTransmitted = False
	opt.SetWorksharingOptions(wsopt)
	OUT = doc.SaveAs(path, opt)