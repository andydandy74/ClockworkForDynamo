# This script is based on code from the node
# DirectShape.ByGeometry from package SpringNodes.
# Thanks Dimitar for doing all the hard work for me... ;-)

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
geometry = UnwrapElement(IN[0])
cat = UnwrapElement(IN[1])
names = IN[2]
counter = 0
elementlist = list()

dsLib = DirectShapeLibrary.GetDirectShapeLibrary(doc)

TransactionManager.Instance.EnsureInTransaction(doc)
for geom in geometry:
	# delete old DS type if the name already exists
	if dsLib.ContainsType(names[counter]):
		old_type = dsLib.FindDefinitionType(names[counter])
		try: doc.Delete(old_type)
		except: pass
	try:
		# create new DS type
		newDStype = DirectShapeType.Create(doc, names[counter], cat.Id)
		newDStype.SetShape(geom)
		dsLib.AddDefinitionType(names[counter], newDStype.Id)
		# create new DS instance
		newDS =  DirectShape.CreateElementInstance(doc, newDStype.Id, cat.Id, names[counter], Transform.Identity)
		newDS.SetTypeId(newDStype.Id)
		elementlist.append(newDS)
	except: elementlist.append(None)
	counter += 1
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist