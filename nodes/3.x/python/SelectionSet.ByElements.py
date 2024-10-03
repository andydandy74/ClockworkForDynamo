import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
name = IN[1]

# create itemset
items = UnwrapElement(IN[0])
ids = list()
for item in items:
	ids.append(item.Id)
itemset = List[ElementId](ids)

# collect all existing filters from the model 
names = list()
collector = FilteredElementCollector(doc)
filters = collector.OfClass(FilterElement).ToElements();

selset = False
TransactionManager.Instance.EnsureInTransaction(doc)
# if a filter of that name already exists, delete its content
for filter in filters:
	if filter.Name == name:
		filter.Clear()
		selset = filter
# create a new selection set if it doesn't already exist
if selset == False:
	selset = SelectionFilterElement.Create(doc,name)
# add the items to the selection set
try: 
	selset.AddSet(itemset)
	OUT = selset.ToDSType(False)
except: OUT = None
TransactionManager.Instance.TransactionTaskDone()
