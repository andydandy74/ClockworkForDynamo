import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
import System.Reflection
import System.AppDomain

rAssembly = [x for x in System.AppDomain.CurrentDomain.GetAssemblies() if x.GetName().Name == 'RevitAPI'][0]
rElement = [x for x in rAssembly.GetTypes() if x.Name == 'Element' and x.Namespace == 'Autodesk.Revit.DB'][0]
OUT = [x for x in rAssembly.GetTypes() if x.IsClass and x.IsSubclassOf(rElement)]