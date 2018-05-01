import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetDesignOptionSet(item):
	try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.OPTION_SET_ID).AsElementId()).ToDSType(True)
	except: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetDesignOptionSet(x) for x in items]
else: OUT = GetDesignOptionSet(items)