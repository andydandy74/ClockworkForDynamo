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
items = UnwrapElement(IN[0])
names = IN[1]

def SetElementName(item, name):
	# family parameters
	if item.GetType().ToString() == "Autodesk.Revit.DB.FamilyParameter":
		try: 
			doc.FamilyManager.RenameParameter(item, name)
			return True
		except: return False
	# regular revit worksets
	elif item.GetType().ToString() =="Autodesk.Revit.DB.Workset":
		try: 
			doc.GetWorksetTable().RenameWorkset(doc, item.Id, name)
			return True
		except: return False
	# non-OOTB implementations (3rd perty e.g. archi-lab)
	elif "Workset" in item.GetType().ToString():
		try: 
			doc.GetWorksetTable().RenameWorkset(doc, WorksetId(item.Id), name)
			return True
		except: return False
	# everything else that has a name property
	else:
		try: 
			item.Name = name
			return True
		except: return False

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(names, list): OUT = [SetElementName(x, y) for x, y in zip(items, names)]
	else: OUT = [SetElementName(x, names) for x in items]
else:
	if isinstance(names, list): OUT = SetElementName(items, names[0])
	else: OUT = SetElementName(items, names)
TransactionManager.Instance.TransactionTaskDone()