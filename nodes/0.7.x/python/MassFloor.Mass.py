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
massfloors = UnwrapElement(IN[0])
elementlist = list()
for item in massfloors:
	try:
		elementlist.append(doc.GetElement(item.OwningMassId).ToDSType(True))
	except:
		elementlist.append(list())
OUT = elementlist