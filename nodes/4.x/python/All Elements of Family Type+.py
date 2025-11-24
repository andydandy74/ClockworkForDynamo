import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def InstancesOfFamilyType(ft, doc):
    collector = FilteredElementCollector(doc)
    try:
        if version > 2024: ftCat = ft.Category.Id.Value
        else: ftCat = ft.Category.Id.IntegerValue
        bic = System.Enum.ToObject(BuiltInCategory, ftCat)
        collector.OfCategory(bic)
        if version > 2024: return [x for x in collector.ToElements() if x.GetTypeId().Value == ft.Id.Value]
        else: return [x for x in collector.ToElements() if x.GetTypeId().IntegerValue == ft.Id.IntegerValue]
    except: return []

famtypes = UnwrapElement(IN[0])
inputdoc = UnwrapElement(IN[2])
version = IN[3]
if not inputdoc: doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance": doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document": doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument

if isinstance(IN[0], list): OUT = [InstancesOfFamilyType(x, doc) for x in famtypes]
else: OUT = InstancesOfFamilyType(famtypes, doc)