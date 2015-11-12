import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

mats = UnwrapElement(IN[0])
colorlist = list()
glowlist = list()
classlist = list()
shinylist = list()
smoothlist = list()
translist = list()

for mat in mats:
	colorlist.append(mat.Color)
	if mat.Glow:
		glowlist.append(True)
	else:
		glowlist.append(False)
	classlist.append(mat.MaterialClass)
	shinylist.append(mat.Shininess)
	smoothlist.append(mat.Smoothness)
	translist.append(mat.Transparency)
OUT = (classlist,colorlist,glowlist,shinylist,smoothlist,translist)