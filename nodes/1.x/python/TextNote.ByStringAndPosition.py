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
width = IN[5]
textalign = IN[6]
version = IN[7]
rotation = IN[8]
textnotetype = UnwrapElement(IN[9])
counter = 0
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for xyz in xyzlist:
	if version > 2016:
		options = TextNoteOptions(textnotetype.Id)
		options.Rotation = rotation
		newtextnote = TextNote.Create(doc, view.Id, xyz, width, text[counter], options)
	else:
		doccreation = doc.Create
		newtextnote = doccreation.NewTextNote(view,xyz,basevecs[counter],upvecs[counter],width,textalign,text[counter])
	elementlist.append(newtextnote)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist