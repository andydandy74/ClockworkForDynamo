import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
elementlist = list()
if doc.IsFamilyDocument:
	for param in doc.FamilyManager.Parameters:
		elementlist.append(param)
OUT = elementlist