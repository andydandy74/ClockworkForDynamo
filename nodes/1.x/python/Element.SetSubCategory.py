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
items = UnwrapElement(IN[0])
subcat = Category.GetCategory(doc,ElementId(IN[1].Id))
gstyletype = IN[2]
if not gstyletype:
	gstyletype = GraphicsStyleType.Projection
else:
	gstyletype = GraphicsStyleType.Cut
gstyle = subcat.GetGraphicsStyle(gstyletype)
success = list()
TransactionManager.Instance.EnsureInTransaction(doc)
for item in items:
	try:
		item.Subcategory = subcat
		success.append(True)
	except:
		try:
			item.Subcategory = gstyle
			success.append(True)
		except:
			try:
				item.LineStyle = gstyle
				success.append(True)
			except:
				success.append(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = (items,success)