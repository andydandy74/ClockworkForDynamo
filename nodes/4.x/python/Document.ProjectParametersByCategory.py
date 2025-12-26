import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

search_cats = UnwrapElement(IN[0])
search_ids = []
names = []
vag = []
pgs = []
pts = []
uts = []
isvis = []
elems = []
guids = []
isinst = []

if not isinstance(IN[0], list): search_cats = [search_cats]
for search_cat in search_cats:
    search_ids.append(search_cat.Id.Value)
    names.append(list())
    vag.append(list())
    pgs.append(list())
    pts.append(list())
    uts.append(list())
    isvis.append(list())
    elems.append(list())
    guids.append(list())
    isinst.append(list())

inputdoc = UnwrapElement(IN[2])
if inputdoc == None:
    doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
    doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
    doc = inputdoc
else: doc = None

iterator = doc.ParameterBindings.ForwardIterator()
while iterator.MoveNext():
    for cat in iterator.Current.Categories:
        i = 0
        catID = cat.Id.Value
        for search_id in search_ids:
            if catID == search_id:
                names[i].append(iterator.Key.Name)
                vag[i].append(iterator.Key.VariesAcrossGroups)
                pts[i].append(iterator.Key.GetDataType())
                pgs[i].append(iterator.Key.GetGroupTypeId())
                isvis[i].append(iterator.Key.Visible)
                elem = doc.GetElement(iterator.Key.Id)
                elems[i].append(elem)
                if elem.GetType().ToString() == 'Autodesk.Revit.DB.SharedParameterElement':
                    guids[i].append(elem.GuidValue)
                else: guids[i].append(None)
                if iterator.Current.GetType().ToString() == 'Autodesk.Revit.DB.InstanceBinding':
                    isinst[i].append(True)
                else: isinst[i].append(False)
            i += 1
if isinstance(IN[0], list): OUT = (names, vag, pgs, pts, isvis, elems, guids, isinst)
else: OUT = (names[0], vag[0], pgs[0], pts[0], isvis[0], elems[0], guids[0], isinst[0])