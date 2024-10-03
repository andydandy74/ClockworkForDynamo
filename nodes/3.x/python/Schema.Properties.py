import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

schemas = IN[0]
OUT = []

def SchemaProperties(schema):
	if hasattr(schema, "SchemaName"): 
		return schema.SchemaName, schema.VendorId, schema.GUID, schema.Documentation, schema.ApplicationGUID, str(schema.ReadAccessLevel), str(schema.WriteAccessLevel)
	else: return None, None, None, None, None, None, None

if isinstance(IN[0], list): OUT = map(list, zip(*[SchemaProperties(x) for x in schemas]))
else: OUT = SchemaProperties(schemas)