import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

arrays = UnwrapElement(IN[0])

def GetArrayMembers(array):
	if hasattr(array, "GetOriginalMemberIds"):
		returnvals = []
		for id in array.GetOriginalMemberIds():
			return array.Document.GetElement(id)
	else: return None

if isinstance(IN[0], list): OUT = [GetArrayMembers(x) for x in arrays]
else: OUT = GetArrayMembers(arrays)