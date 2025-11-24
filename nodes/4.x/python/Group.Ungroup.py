import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def UngroupGroup(group, extractMembers):
	success = False
	members = []
	if hasattr(group, "UngroupMembers"):
		try:
			ids = group.UngroupMembers()
			if extractMembers: members = [group.Document.GetElement(x) for x in ids]
			success = True
		except: pass
	return members, success

doc = DocumentManager.Instance.CurrentDBDocument
groups = UnwrapElement(IN[0])
TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list): 
	if len(groups) > 0: OUT = map(list, zip(*[UngroupGroup(x, IN[1]) for x in groups]))
	else: OUT = ([], [])
else: OUT = UngroupGroup(groups, IN[1])
TransactionManager.Instance.TransactionTaskDone()