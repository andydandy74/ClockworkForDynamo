import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

if isinstance(IN[0], list): paths = IN[0]
else: paths = [IN[0]]
APIversion = IN[1]

bfi = [BasicFileInfo.Extract(x) for x in paths]
username = [x.Username for x in bfi]
language = [x.LanguageWhenSaved for x in bfi]
if APIversion > 2019: version = [x.Format for x in bfi]
else: version = [x.SavedInVersion for x in bfi]
versioncurrent = [x.IsSavedInCurrentVersion for x in bfi]
if APIversion > 2016: versionlater = [x.IsSavedInLaterVersion for x in bfi]
else: versionlater = [None for x in bfi]
workshared = [x.IsWorkshared for x in bfi]
local = [x.IsLocal for x in bfi]
central = [x.IsCentral for x in bfi]
centralpath = [x.CentralPath for x in bfi]

if isinstance(IN[0], list):
	OUT = username, language, version, versioncurrent, versionlater, workshared, local, central, centralpath
else:
	OUT = username[0], language[0], version[0], versioncurrent[0], versionlater[0], workshared[0], local[0], central[0], centralpath[0]