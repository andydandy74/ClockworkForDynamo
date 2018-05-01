import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetSheetSetViews(set):
	if hasattr(set, 'Views'):
		return [x.ToDSType(True) for x in set.Views]
	else: return []

viewsheetsets = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetSheetSetViews(x) for x in viewsheetsets]
else: OUT = GetSheetSetViews(viewsheetsets)