#Clockwork for Dynamo - Version History

##0.75.5

###Improvements:
- Document.ProjectPosition now outputs lengths instead of doubles
- List.ReplaceItemAtIndex now takes a list of indices

###Fixes:
- Repaired StructuralFoundation.KindIsIsolated, StructuralFoundation.KindIsSlab & StructuralFoundation.KindIsWallFooting

##0.75.4

###New nodes:
- Buckyball.ByOriginAndRadius
- Buckyball.Coordinates
- Buckyball.Struts
- Buckyball.Surfaces
- Geometry.ClosestTo
- Geometry.FurthestFrom
- RevitColor.FromDynamoColor

###Improvements:
- Element.Level now also retrieves the levels of plan views

###Fixes:
- DoorOrWindow.ExitsToOneRoomOnly now actually works properly...

##0.75.3

###Improvements:
- Room.Boundaries now outputs Dynamo curves instead of Revit curves

##0.75.2

###New nodes:
- String.FindRegularExpression
- String.ReplaceRegularExpression
- String.SplitByRegularExpression

###Improvements:
- Element.Host will now also find hosts of WallSweeps

##0.75.1

###New nodes:
- Element.OverrideTransparencyInView
- ElementType.Duplicate
- Material.Duplicate
- Math.NormalizeRange
- PerspectiveView.OrientToEyeAndTargetPosition
- SolarAnalysisType.Average
- SolarAnalysisType.Cumulative
- SolarAnalysisType.Peak

###Improvements/changes:
- Migrated several node-based custom nodes to CBN-based in order to improve performance
- Relabeled some of the custom nodes
- Renamed Element.CompoundStructureLayers to FamilyType.CompoundStructureLayers

###Deprecated nodes:
- SolarRadiationCSV.Parse

##0.74.3

###New nodes:
- Element.CompoundStructureLayers
- UV.Average

##0.74.2

###New nodes:
- Point.Average
- Vector.Average

##0.74.1

###New nodes:
- DividedSurface.HorizontalIntersectsByEndpoints
- DividedSurface.HorizontalIntersectsByEndpointsAnd Function
- DividedSurface.VerticalIntersectsByEndpoints
- DividedSurface.VerticalIntersectsByEndpointsAnd Function
- Document.SaveAs
- FamilyInstance.CopingElements
- FamilyInstance.AddCoping
- FamilyInstance.RemoveCoping
- List.ReplaceItemAtIndex
- Surface.IsPlanar
- Surface.Vertices
- UV.PruneDuplicates
- Vector.PruneDuplicates
- View3D.IsLocked

###Deprecated nodes:
- Directory.FromFilePath - Use Directory.FromPath instead
- Elements.RemoveDuplicates - Use List.UniqueItems instead (it will now remove duplicate Revit elements from a list as well)

##0.73.2

###New nodes:
- Document.DimensionTypes
- List.RandomElements
- Math.RandomIntegerList
- SelectionSet.ByElements
- TextNote.ByStringAndPosition

###Fixes:
- Element.Inserts now returns a single list of elements when fed a single element
- FamilyInstance.SetType now takes a list of types 

##0.73.1
First (more or less) complete edition for Dynamo 0.7.x

##0.63.3
First complete edition for Dynamo 0.6.3