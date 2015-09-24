import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

faminsts = IN[0]
elementlist = list()
for item in faminsts:
	try:
		n = UnwrapElement(item).Name
	except:
		n = None
	if n == None:
		try:
			n = item.Name
		except:
			n = []
	elementlist.append(n)
OUT = elementlist
