import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
cat = UnwrapElement(IN[0])
subcatname = IN[1]

try:
	OUT = cat.SubCategories.get_Item(subcatname)
except:
	TransactionManager.Instance.EnsureInTransaction(doc)
	OUT = doc.Settings.Categories.NewSubcategory(cat, subcatname)
	TransactionManager.Instance.TransactionTaskDone()