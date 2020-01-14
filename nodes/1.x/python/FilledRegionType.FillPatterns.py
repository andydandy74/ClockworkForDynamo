import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def GetFillPatterns(frt):
	foreground = None
	background = None
	if hasattr(frt, "ForegroundPatternId"):
		if frt.ForegroundPatternId.IntegerValue > 0:
			foreground = frt.Document.GetElement(frt.ForegroundPatternId)
		if frt.BackgroundPatternId.IntegerValue > 0:
			background = frt.Document.GetElement(frt.BackgroundPatternId)
	elif hasattr(frt, "FillPatternId"):	
		if frt.FillPatternId.IntegerValue > 0:
			foreground = frt.Document.GetElement(frt.FillPatternId)
	return foreground, background

filledregiontypes = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = list(map(list, zip(*[GetFillPatterns(x) for x in filledregiontypes])))
else: OUT = GetFillPatterns(filledregiontypes)