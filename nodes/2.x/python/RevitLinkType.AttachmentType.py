import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

links = UnwrapElement(IN[0])

def GetAttachmentType(link):
	if hasattr(link, "AttachmentType"): return link.AttachmentType.ToString()
	else: return None

if isinstance(IN[0], list): OUT = [GetAttachmentType(x) for x in links]
else: OUT = GetAttachmentType(links)