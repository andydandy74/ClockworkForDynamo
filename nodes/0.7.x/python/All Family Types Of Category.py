import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
cats = IN[0]

elementlist = list()
# This could be more elegant if only I knew how to implement a Multicategory filter in Python....
for item in cats:
	collector = FilteredElementCollector(doc)
	collector.OfClass(FamilySymbol)
	bic = System.Enum.ToObject(BuiltInCategory, item.Id)
	collector.OfCategory(bic)
	elementlist.append(collector.ToElements())
OUT = elementlist