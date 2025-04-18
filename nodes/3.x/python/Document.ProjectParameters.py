import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

inputdoc = UnwrapElement(IN[1])
if inputdoc == None:
    doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
    doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
    doc = inputdoc
else: doc = None
version = IN[2]

names = []
cats = []
vag = []
pgs = []
pts = []
uts = []
isvis = []
elems = []
guids = []
isinst = []
bics = []
iterator = doc.ParameterBindings.ForwardIterator()
while iterator.MoveNext():
    vag.append(iterator.Key.VariesAcrossGroups)
    names.append(iterator.Key.Name)
    pts.append(iterator.Key.GetDataType())
    pgs.append(iterator.Key.GetGroupTypeId())
    isvis.append(iterator.Key.Visible)
    elem = doc.GetElement(iterator.Key.Id)
    elems.append(elem)
    if elem.GetType().ToString() == 'Autodesk.Revit.DB.SharedParameterElement':
        guids.append(elem.GuidValue)
    else: guids.append(None)
    if iterator.Current.GetType().ToString() == 'Autodesk.Revit.DB.InstanceBinding':
        isinst.append(True)
    else:
        isinst.append(False)
    thesecats = []
    builtincats = []
    for cat in iterator.Current.Categories:
        if version > 2024: catID = cat.Id.Value
        else: catID = cat.Id.IntegerValue
        try: thesecats.append(Revit.Elements.Category.ById(catID))
        except:
            # Return null if category is not supported by Dynamo
            # This way the user knows there are unsupported categories assigned
            thesecats.append(None)
        builtincats.append(System.Enum.GetName(BuiltInCategory, catID))
    cats.append(thesecats)
    bics.append(builtincats)
OUT = (names,cats,vag, pgs, pts, isvis, elems, guids, isinst, bics)