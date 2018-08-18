import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

relStandardWS = IN[0]
relViewWS = IN[1]
relFamWS = IN[2]
relUserWS = IN[3]
relCheckedOutElems = IN[4]
compact = IN[5]
saveLocalBefore = IN[6]
saveLocalAfter = IN[7]
comment = IN[8]
runme = IN[9]

if runme:
	doc = DocumentManager.Instance.CurrentDBDocument
	tOptions = TransactWithCentralOptions()
	rOptions = RelinquishOptions(False)
	rOptions.StandardWorksets = relStandardWS
	rOptions.ViewWorksets = relViewWS
	rOptions.FamilyWorksets = relFamWS
	rOptions.UserWorksets = relUserWS
	rOptions.CheckedOutElements = relCheckedOutElems
	sOptions = SynchronizeWithCentralOptions()
	sOptions.SetRelinquishOptions(rOptions)
	sOptions.Compact = compact
	sOptions.SaveLocalBefore = saveLocalBefore
	sOptions.SaveLocalAfter = saveLocalAfter
	sOptions.Comment = comment
	TransactionManager.Instance.ForceCloseTransaction()
	try:
		doc.SynchronizeWithCentral(tOptions, sOptions)
		OUT = True
	except:
		OUT = False
else: OUT = False