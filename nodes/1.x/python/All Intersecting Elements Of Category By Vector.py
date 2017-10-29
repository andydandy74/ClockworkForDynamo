import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
theview = UnwrapElement(IN[0])
cat = System.Enum.ToObject(BuiltInCategory, IN[1].Id)
vstart = [x.ToXyz() for x in IN[2]]
vend = [x.ToXyz() for x in IN[3]]

intersectorlist = list()
counter = 0
filter = ElementCategoryFilter(cat)

while counter < len(vstart):
	ThisReferenceArr = ReferenceIntersector(filter, FindReferenceTarget.All, theview)
	found = ThisReferenceArr.Find(vstart[counter], vend[counter])
	foundreferences = list()
	for item in found:
		foundreferences.append(doc.GetElement(item.GetReference()))
	intersectorlist.append(foundreferences)
	counter += 1
OUT = intersectorlist