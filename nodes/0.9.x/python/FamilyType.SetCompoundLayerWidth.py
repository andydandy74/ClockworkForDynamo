import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
famtypes = UnwrapElement(IN[0])
indices = IN[1]
widths = IN[2]
booleans = list()
counter = 0

TransactionManager.Instance.EnsureInTransaction(doc)
for ft in famtypes:
	try:
		cs = ft.GetCompoundStructure()
		cs.SetLayerWidth(indices[counter],widths[counter])
		ft.SetCompoundStructure(cs)
		booleans.append(True)
	except:
		booleans.append(False)
	counter += 1	
TransactionManager.Instance.TransactionTaskDone()

OUT = (famtypes,booleans)