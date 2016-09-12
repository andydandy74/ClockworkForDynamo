import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
collector = FilteredElementCollector(doc)
desopts = collector.OfClass(DesignOption).ToElements()
OUT = desopts