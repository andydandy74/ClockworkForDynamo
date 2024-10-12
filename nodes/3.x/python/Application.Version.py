import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.ApplicationServices import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
if int(app.VersionNumber) > 2017: fullVersion = app.SubVersionNumber
else: fullVersion = str(app.VersionNumber)

OUT = app.VersionName, int(app.VersionNumber), app.VersionBuild, System.Enum.GetName(LanguageType, app.Language), fullVersion