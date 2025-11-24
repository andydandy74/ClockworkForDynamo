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
fullVersion = app.SubVersionNumber

OUT = app.VersionName, int(app.VersionNumber), app.VersionBuild, System.Enum.GetName(LanguageType, app.Language), fullVersion