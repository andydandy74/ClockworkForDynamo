import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
cat = UnwrapElement(IN[0])
subcatname = IN[1]
subcat = [x for x in cat.SubCategories if x.Name == subcatname]
if len(subcat) == 1: subcat = subcat[0]
else:
	TransactionManager.Instance.EnsureInTransaction(doc)
	try: subcat = doc.Settings.Categories.NewSubcategory(cat, subcatname)
	except: subcat = None
	TransactionManager.Instance.TransactionTaskDone()
OUT = subcat