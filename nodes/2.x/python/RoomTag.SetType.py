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

def SetRoomTagType(tag,tagtype):
	if hasattr(tag, "RoomTagType"):
		tag.RoomTagType = tagtype
		return True
	else: return False

doc = DocumentManager.Instance.CurrentDBDocument
tags = UnwrapElement(IN[0])
tagtypes = UnwrapElement(IN[1])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[1], list): OUT = [SetRoomTagType(x,y) for x,y in zip(tags,tagtypes)]
	else: OUT = [SetRoomTagType(x,tagtypes) for x in tags]
else:
	if isinstance(IN[1], list): OUT = SetRoomTagType(tags,tagtypes[0])
	else: OUT = SetRoomTagType(tags,tagtypes)
TransactionManager.Instance.TransactionTaskDone()