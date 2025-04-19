import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk
import System

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

items = UnwrapElement(IN[0])
unittype = ForgeTypeId('autodesk.spec.aec:area-2.0.0')
version = IN[1]

def InternalUnitToDisplayUnit(val, unittype):
    formatoptions = doc.GetUnits().GetFormatOptions(unittype)
    dispunits = formatoptions.GetUnitTypeId()
    try: return UnitUtils.ConvertFromInternalUnits(val,dispunits)
    except: return None

def RoomFinishes(item):
    doc = item.Document
    calculator = SpatialElementGeometryCalculator(doc)
    options = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
    # get boundary location from area computation settings
    boundloc = Autodesk.Revit.DB.AreaVolumeSettings.GetAreaVolumeSettings(doc).GetSpatialElementBoundaryLocation(SpatialElementType.Room)
    options.SpatialElementBoundaryLocation = boundloc
    mlist = []
    tlist = []
    elist = []
    alist = []
    flist = []
    try:
        results = calculator.CalculateSpatialElementGeometry(item)
        for face in results.GetGeometry().Faces:
            for bface in results.GetBoundaryFaceInfo(face):
                beface = bface.GetBoundingElementFace()
                if beface:
                    if version > 2024: befaceMatId = beface.MaterialElementId.Value
                    else: befaceMatId = beface.MaterialElementId.IntegerValue
                tlist.append(System.Enum.GetName(SubfaceType, bface.SubfaceType))
                eId = bface.SpatialBoundaryElement.HostElementId
                if eId == ElementId.InvalidElementId:
                    liId = bface.SpatialBoundaryElement.LinkInstanceId
                    if liId == ElementId.InvalidElementId: 
                        elist.append(None)
                        mlist.append(None)
                    else:
                        leId = bface.SpatialBoundaryElement.LinkedElementId
                        if leId == ElementId.InvalidElementId: 
                            elist.append(None)
                            mlist.append(None)
                        else: 
                            elist.append(doc.GetElement(liId).GetLinkDocument().GetElement(leId))
                            if beface:
                                if befaceMatId == -1: mlist.append(None)
                                else: mlist.append(doc.GetElement(liId).GetLinkDocument().GetElement(beface.MaterialElementId))
                            else: mlist.append(None)
                else: 
                    elist.append(doc.GetElement(eId))
                    if beface:
                        if befaceMatId == -1: mlist.append(None)
                        else: mlist.append(doc.GetElement(beface.MaterialElementId))
                    else: mlist.append(None)
                alist.append(InternalUnitToDisplayUnit(bface.GetSubface().Area, unittype))
                flist.append(bface.GetBoundingElementFace())
        return tlist, mlist, alist, flist, elist
    except: return [],[],[],[],[]

if isinstance(IN[0], list): 
    results = [RoomFinishes(x) for x in items]
    OUT = list(zip(*results))
else: OUT = RoomFinishes(items)