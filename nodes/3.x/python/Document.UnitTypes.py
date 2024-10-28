import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

OUT = UnitUtils.GetAllMeasurableSpecs(), [x.TypeId for x in UnitUtils.GetAllMeasurableSpecs()]