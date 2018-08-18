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

doc = DocumentManager.Instance.CurrentDBDocument
famtypes = IN[0]
newnames = IN[1]
elementlist = [] 
func_enum = {'Revit.Elements.WallType' : Revit.Elements.WallType.ByName,
			 'Revit.Elements.FloorType' : Revit.Elements.FloorType.ByName,
			 'Revit.Elements.FamilyType' : Revit.Elements.FamilyType.ByName}

TransactionManager.Instance.EnsureInTransaction(doc)
for i in xrange(len(famtypes) ):
	try:
		elementlist.append(UnwrapElement(famtypes[i]).Duplicate(newnames[i]) )
	except:
		try:
			t1 = famtypes[i].GetType().ToString()
			if t1 in func_enum:
				elementlist.append(func_enum[t1](newnames[i]) )
			else:
				elementlist.append(None)
		except:
			elementlist.append(None)

TransactionManager.Instance.TransactionTaskDone()
OUT = elementlist