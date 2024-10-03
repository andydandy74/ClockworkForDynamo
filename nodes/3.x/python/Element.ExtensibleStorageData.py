import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def ReadESData(item, schema, fields, valtypes):
	if hasattr(item, "GetEntity"):
		ent =  item.GetEntity(schema)
		return [ent.Get[y](x) for x, y in zip(fields,valtypes)]
	else: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = map(list, zip(*[ReadESData(x, IN[1], IN[2], IN[3]) for x in items]))
else: OUT = ReadESData(items, IN[1], [2], IN[3])