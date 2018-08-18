import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

inputdoc = UnwrapElement(IN[1])
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
	doc = inputdoc.GetLinkDocument()
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = None

elementlist = list()
projinfo = doc.ProjectInformation
elementlist.append(projinfo.OrganizationName)
elementlist.append(projinfo.OrganizationDescription)
elementlist.append(projinfo.BuildingName)
# this property seems to be missing in some files - weird...
try:
	elementlist.append(projinfo.Author)
except:
	elementlist.append(None)
elementlist.append(projinfo.IssueDate)
elementlist.append(projinfo.Status)
elementlist.append(projinfo.ClientName)
elementlist.append(projinfo.Address)
elementlist.append(projinfo.Name)
elementlist.append(projinfo.Number)
OUT = elementlist