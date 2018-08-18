import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetText(item):
	if hasattr(item, "Text"): return item.Text
	else: return None

textnotes = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetText(x) for x in textnotes]
else: OUT = GetText(textnotes)