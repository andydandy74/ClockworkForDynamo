import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

footingtypes = UnwrapElement(IN[0])
booleans = list()
for item in footingtypes:
	try:
		footingbreaks = item.get_Parameter(BuiltInParameter.CONTINUOUS_FOOTING_BREAK_AT_INSERTS_DISABLE).AsInteger()
		if footingbreaks == 0: booleans.append(True)
		elif footingbreaks == 1: booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans