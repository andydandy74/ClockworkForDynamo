import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def FieldProperties(field):
	if hasattr(field, "FieldName"):
		if version > 2021: utype = field.GetSpecTypeId()
		else:  utype = field.UnitType
		return field.FieldName, field.Documentation, field.ContainerType, utype, field.ValueType, field.SubSchema, field.SubSchemaGUID
	else: return None, None, None, None, None, None, None

fields = IN[0]
version = IN[1]

if isinstance(IN[0], list): OUT = map(list, zip(*[FieldProperties(x) for x in fields]))
else: OUT = FieldProperties(fields)