import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

faminsts = UnwrapElement(IN[0])
elementlist = list()
for item in faminsts:
	try:	
		elementlist.append(item.Document.GetElement(item.LevelId).ToDSType(True))
	except:
		try:
			elementlist.append(item.Level.ToDSType(True))
		except:
			try:
				elementlist.append(item.GenLevel.ToDSType(True))
			except:
				elementlist.append(list())
OUT = elementlist