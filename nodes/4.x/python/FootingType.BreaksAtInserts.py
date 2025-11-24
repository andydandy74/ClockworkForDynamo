import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def FTBreaksAtInsert(ft):
	try:
		footingbreaks = ft.get_Parameter(BuiltInParameter.CONTINUOUS_FOOTING_BREAK_AT_INSERTS_DISABLE).AsInteger()
		if footingbreaks == 0: return True
		else: return False
	except: return False

ftypes = UnwrapElement(IN[0])
if isinstance(IN[0], list): OUT = [FTBreaksAtInsert(x) for x in ftypes]
else: OUT = FTBreaksAtInsert(ftypes)