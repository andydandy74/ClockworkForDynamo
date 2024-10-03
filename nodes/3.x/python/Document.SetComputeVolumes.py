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
compvol = IN[0]
compvolstate = IN[1]

if compvol != compvolstate:
	TransactionManager.Instance.EnsureInTransaction(doc)
	try:
		AreaVolumeSettings.GetAreaVolumeSettings(doc).ComputeVolumes = compvol
		OUT = True
	except: OUT = False
	TransactionManager.Instance.TransactionTaskDone()
else: OUT = True