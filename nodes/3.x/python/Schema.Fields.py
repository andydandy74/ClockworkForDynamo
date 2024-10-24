import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def SchemaFields(schema):
	if hasattr(schema, "ListFields"):
		if schema.ReadAccessGranted(): return schema.ListFields()
		else: return []
	else: return []

schemas = IN[0]

if isinstance(IN[0], list): OUT =[SchemaFields(x) for x in schemas]
else: OUT = SchemaFields(schemas)