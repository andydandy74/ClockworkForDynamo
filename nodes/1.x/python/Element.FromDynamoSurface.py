import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def ElementByFace(face, doc):
	try: return doc.GetElement(face.Tags.LookupTag("RevitFaceReference"))
	except: return None

doc = DocumentManager.Instance.CurrentDBDocument
faces = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [ElementByFace(x, doc) for x in faces]
else: OUT = ElementByFace(faces, doc)