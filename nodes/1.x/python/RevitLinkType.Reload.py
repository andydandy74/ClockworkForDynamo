import clr
import sys
sys.path.append("C:\Program Files (x86)\IronPython 2.7\Lib")
import os.path

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def ReloadLink(doc, link, path):
	try:
		if path:
			if os.path.isfile(path):
				bfi = BasicFileInfo.Extract(path)
				if not bfi.IsSavedInLaterVersion:
					if path == doc.PathName:
						link.Reload()
					else:
						mpath = ModelPathUtils.ConvertUserVisiblePathToModelPath(path)
						wsconfig = WorksetConfiguration()
						link.LoadFrom(mpath, wsconfig)
					return True
				else: return False
			else: return False
		elif link.LocallyUnloaded: 
			link.RevertLocalUnloadStatus()
			return True
		else: 
			link.Reload()
			return True
	except:
		return False
		
doc = DocumentManager.Instance.CurrentDBDocument
linktypes = UnwrapElement(IN[0])
paths = IN[1]
booleans = list()

TransactionManager.Instance.ForceCloseTransaction()
if isinstance(IN[0], list): 
	if isinstance(IN[1], list): OUT = [ReloadLink(doc, x, y) for x, y in zip(linktypes, paths)]
	else: OUT = [ReloadLink(doc, x, paths) for x in linktypes]
else: OUT = ReloadLink(doc, linktypes, paths)