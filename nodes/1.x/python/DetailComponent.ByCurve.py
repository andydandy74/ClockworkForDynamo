import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
curves = UnwrapElement(IN[0])
famtype = UnwrapElement(IN[1])
view = UnwrapElement(IN[2])
version = IN[3]
elementlist = list()
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
for curve in curves:
	if version > 2015:
		if not(famtype.IsActive): famtype.Activate()
	try:
		newobj = doc.Create.NewFamilyInstance(curve.ToRevitType(),famtype,view)
		elementlist.append(newobj.ToDSType(False))
	except:
		elementlist.append(None)
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist