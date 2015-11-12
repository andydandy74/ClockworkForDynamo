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
	# Use a built-in property of (wrapped) Dynamo elements for family symbols instead
	if n == None:
		try:
			n = item.Name
		except:
			n = []
	elementlist.append(n)
OUT = elementlist