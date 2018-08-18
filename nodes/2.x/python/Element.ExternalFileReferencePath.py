import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetExtFileRefPath(item):
	try: return ModelPathUtils.ConvertModelPathToUserVisiblePath(item.GetExternalFileReference().GetAbsolutePath())
	except: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetExtFileRefPath(x) for x in items]
else: OUT = GetExtFileRefPath(items)