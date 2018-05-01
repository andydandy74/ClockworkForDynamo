import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetLevel(item):
	if hasattr(item, "LevelId"): return item.Document.GetElement(item.LevelId)
	elif hasattr(item, "Level"): return item.Level
	elif hasattr(item, "GenLevel"): return item.GenLevel
	else:
		try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_REFERENCE_LEVEL_PARAM).AsElementId())
		except: 
			try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM).AsElementId())
			except: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetLevel(x) for x in items]
else: OUT = GetLevel(items)