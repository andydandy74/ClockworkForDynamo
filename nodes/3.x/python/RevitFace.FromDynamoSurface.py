import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def RevitFaceFromDynamoFace(dface):
	try:
		ref = dface.Tags.LookupTag("RevitFaceReference")
		return doc.GetElement(ref).GetGeometryObjectFromReference(ref)
	except: return None

doc = DocumentManager.Instance.CurrentDBDocument
faces = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [RevitFaceFromDynamoFace(x) for x in faces]
else: OUT = RevitFaceFromDynamoFace(faces)