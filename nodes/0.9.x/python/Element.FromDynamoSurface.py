import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
faces = UnwrapElement(IN[0])
elementlist = list()
for face in faces:
	try:
		ref = face.Tags.LookupTag("RevitFaceReference")
		elem = doc.GetElement(ref)
		elementlist.append(elem)
	except:
		elementlist.append(list())
OUT = elementlist