import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

element = UnwrapElement(IN[0])
params = IN[1]
elementlist = list()
for paramname in params:
	try:
		for param in element.Parameters:
			if param.Definition.Name == paramname:
				if param.IsReadOnly:
					elementlist.append(True)
				else:
					elementlist.append(False)
	except:
		elementlist.append(False)
OUT = elementlist