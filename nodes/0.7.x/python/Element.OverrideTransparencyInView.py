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
view = UnwrapElement(IN[1])
trans = IN[2]
elementlist = list()

override = OverrideGraphicSettings()
override.SetSurfaceTransparency(trans)

TransactionManager.Instance.EnsureInTransaction(doc)
for item in items:
	view.SetElementOverrides(item.Id, override)
TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist