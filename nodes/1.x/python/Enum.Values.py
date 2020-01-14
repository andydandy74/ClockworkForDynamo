import clr
import System
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
import Autodesk

rAssembly = [x for x in System.AppDomain.CurrentDomain.GetAssemblies() if x.GetName().Name == 'RevitAPI'][0]

def GetEnumValues(typename):
	foundenums = [x for x in rAssembly.GetTypes() if x.Name == typename and x.BaseType == System.Enum]
	try:
		enumnames = foundenums[0].GetEnumNames()
		enumvals = [int(System.Enum.Parse(foundenums[0], x)) for x in enumnames]
		return (enumnames, enumvals)
	except: return ([], [])

enums = IN[0]

if isinstance(IN[0], list): OUT = map(list, zip(*[GetEnumValues(x) for x in enums]))
else: OUT = GetEnumValues(enums)