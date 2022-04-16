import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def SetCompoundLayerMaterial(famtype, index, mat):
	try:
		cs = famtype.GetCompoundStructure()
		cs.SetMaterialId(index,mat.Id)
		famtype.SetCompoundStructure(cs)
		return True
	except: return False

doc = DocumentManager.Instance.CurrentDBDocument
famtypes = UnwrapElement(IN[0])
indices = IN[1]
mats = UnwrapElement(IN[2])

TransactionManager.Instance.EnsureInTransaction(doc)
if isinstance(IN[0], list):
	if isinstance(IN[2], list):
		if isinstance(IN[1], list): OUT = [SetCompoundLayerMaterial(x,y,z) for x,y,z in zip(famtypes, indices, mats)]
		else: OUT = [SetCompoundLayerMaterial(x,indices,y) for x,y in zip(famtypes, mats)]
	else:
		if isinstance(IN[1], list): OUT = [SetCompoundLayerMaterial(x,y,mats) for x,y in zip(famtypes, indices)]
		else: OUT = [SetCompoundLayerMaterial(x,indices,mats) for x in famtypes]
else:
	if isinstance(IN[2], list):
		if isinstance(IN[1], list): OUT = [SetCompoundLayerMaterial(famtypes,x,y) for x,y in zip(indices, mats)]
		else: OUT = [SetCompoundLayerMaterial(famtypes,indices,x) for x in mats]
	else:
		if isinstance(IN[1], list): OUT = [SetCompoundLayerMaterial(famtypes,x,mats) for x in indices]
		else: OUT = SetCompoundLayerMaterial(famtypes,indices,mats)
TransactionManager.Instance.TransactionTaskDone()