import clr

rooms = IN[0]
doors = IN[1]
fromroom = IN[2]
toroom = IN[3]
elementlist = list()

i = 0
while i < (len(rooms)-1):
	j = 0
	while j < len(doors):
		if (rooms[i] == fromroom[j] and rooms[i+1] == toroom[j]) or (rooms[i+1] == fromroom[j] and rooms[i] == toroom[j]):
			elementlist.append(doors[j])
		j += 1
	i += 1
OUT = elementlist

##### NEXT PYTHON NODE #####

import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

elementlist = list()
collector = FilteredElementCollector(doc)
collector.OfClass(FamilyInstance)
collector.OfCategory(BuiltInCategory.OST_Doors)

OUT = collector.ToElements()