import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
import Autodesk

rAssembly = [x for x in System.AppDomain.CurrentDomain.GetAssemblies() if x.GetName().Name == 'RevitAPI'][0]
OUT = [x.Name for x in rAssembly.GetTypes() if x.Namespace is not None and x.Namespace.startswith("Autodesk.Revit.") and x.BaseType == System.Enum]
OUT = sorted(OUT, key=str.lower)