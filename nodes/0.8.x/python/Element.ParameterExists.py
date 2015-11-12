# This node was originally created by Andreas Dieckmann
# and only updated by Konrad K Sobon to work with Revit 2016

# Copyright(c) 2015, Konrad K Sobon
# @arch_laboratory, http://archi-lab.net

# Modified to Clockwork coding style by Andreas Dieckmann

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

items = UnwrapElement(IN[0])
param = IN[1]
elementList = []

for item in items:
	try:
		params = item.Parameters
		paramNames = [i.Definition.Name for i in params]
		if param in paramNames:
			elementList.append(True)
		else:
			elementList.append(False)
	except:
		elementList.append(False)

OUT = elementList