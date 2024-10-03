import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def DuplicateFamType(famtype, name):
	try:
		return famtype.Duplicate(name)
	except:
		try:
			t1 = famtype.GetType().ToString()
			if t1 in func_enum: return func_enum[t1](name)
			else: return None
		except:
			return None

doc = DocumentManager.Instance.CurrentDBDocument
famtypes = IN[0]
newnames = IN[1]
func_enum = {'Revit.Elements.WallType' : Revit.Elements.WallType.ByName,
			 'Revit.Elements.FloorType' : Revit.Elements.FloorType.ByName,
			 'Revit.Elements.FamilyType' : Revit.Elements.FamilyType.ByName}

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(famtypes, list): OUT = [DuplicateFamType(x, y) for x, y in zip(famtypes, newnames)]
else: OUT = DuplicateFamType(famtypes, newnames)
TransactionManager.Instance.TransactionTaskDone()