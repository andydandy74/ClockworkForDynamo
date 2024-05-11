import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

def GetRevitFaceRef(face):
	try: 
		ref = face.Tags.LookupTag("RevitFaceReference")
		try: stableref = ref.ConvertToStableRepresentation(doc)
		except: stableref = None
		return ref, stableref
	except: return None, None

doc = DocumentManager.Instance.CurrentDBDocument
faces = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = list(zip(*[GetRevitFaceRef(x) for x in faces]))
else: OUT = GetRevitFaceRef(faces)