import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def WallCreationMethod(wall):
	typename = wall.GetType().Name
	if typename == 'Wall': return 'Standard'
	elif typename == 'FaceWall': return 'By Face'
	elif typename == 'FamilyInstance': return 'In-Place'
	else: return None

walls = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [WallCreationMethod(x) for x in walls]
else: OUT = WallCreationMethod(walls)