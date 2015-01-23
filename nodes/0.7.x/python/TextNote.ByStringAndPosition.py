import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = UnwrapElement(IN[0])
xyzlist = [x.ToXyz() for x in IN[1]]
basevecs = [x.ToXyz() for x in IN[2]]
upvecs = [x.ToXyz() for x in IN[3]]
text = IN[4]
doccreation = doc.Create
counter = 0
textalign = TextAlignFlags.TEF_ALIGN_LEFT
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for xyz in xyzlist:
	newtextnote = doccreation.NewTextNote(view,xyz,basevecs[counter],upvecs[counter],0,textalign,text[counter])
	elementlist.append(newtextnote)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist