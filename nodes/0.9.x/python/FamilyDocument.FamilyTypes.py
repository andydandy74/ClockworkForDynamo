import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
elementlist = list()
for ftype in doc.FamilyManager.Types:
	elementlist.append(ftype)
OUT = elementlist