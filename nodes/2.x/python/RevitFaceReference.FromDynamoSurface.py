import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

faces = UnwrapElement(IN[0])
elementlist = list()
for face in faces:
	try:
		ref = face.Tags.LookupTag("RevitFaceReference")
		elementlist.append(ref)
	except:
		elementlist.append(list())
OUT = elementlist