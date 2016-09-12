import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

params = UnwrapElement(IN[0])
elementlist = list()
for param in params:
	# in Revit 2016 R2 or later
	try:
		# any params that do not have a unit
		if str(param.GetDefinition().UnitType) == "UT_Number":
			# booleans
			if str(param.GetDefinition().ParameterType) == "YesNo":
				elementlist.append(param.GetValue().Value == 1)
			# parameter types that contain element ids
			elif str(param.GetDefinition().ParameterType) == "Image" or str(param.GetDefinition().ParameterType) == "Material":
				elementlist.append(param.Document.GetElement(param.GetValue().Value))
			# everything else
			else:
				elementlist.append(param.GetValue().Value)
		# any params with units: convert vals to display unit
		else:
			formatoptions = doc.GetUnits().GetFormatOptions(param.GetDefinition().UnitType)
			elementlist.append(UnitUtils.ConvertFromInternalUnits(param.GetValue().Value,formatoptions.DisplayUnits))
	# any earlier Revit version does not support gloabl params
	except:
		elementlist.append(list())
OUT = elementlist