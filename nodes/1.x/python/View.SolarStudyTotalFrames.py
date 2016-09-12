import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
elementlist = []
for view in views:
	try:
		elementlist.append(view.SunAndShadowSettings.NumberOfFrames)
	except:
		elementlist.append(0)
OUT = elementlist