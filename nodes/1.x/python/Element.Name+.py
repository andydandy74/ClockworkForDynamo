import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

faminsts = IN[0]
elementlist = list()
for item in faminsts:
	try:
		n = UnwrapElement(item).Name
	except:
		# Use a built-in property of (wrapped) Dynamo elements for family symbols instead
		try:
			n = item.Name
		except:
			# maybe it's a parameter name
			try:
				n = item.Definition.Name
			except:
				n = []
	elementlist.append(n)
OUT = elementlist