import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
faminsts = UnwrapElement(IN[0])
elementlist = list()
for item in faminsts:
	try:	
		elementlist.append(doc.GetElement(item.LevelId).ToDSType(True))
	except:
		try:
			elementlist.append(item.Level.ToDSType(True))
		except:
			try:
				elementlist.append(item.GenLevel.ToDSType(True))
			except:
				elementlist.append(list())
OUT = elementlist