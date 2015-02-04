#Clockwork for Dynamo - Version History

##0.75.16

##New nodes:
- FamilyInstance.SubComponents
- FamilyInstance.SuperComponent

##Improvements/Changes:
- Recategorized and relabeled some nodes
- Material.Properties now returns single outputs for single inputs

##0.75.15

##New nodes:
- Element.ResetOverridesInView
- List.ReplaceEmptyLists
- List.ReplaceNull
- Plane.ByBestFitFromFace

###Improvements:
- All Elements Of Name now has a separate outport for the first result in the list
- List.GroupListOfListsByKey now returns transposed sublists for better readability
- PlaceholderSheet.ByNumberAndName now accepts strings *or* numbers as sheet numbers
- Document.Path now actually does return the directory, too
- Fixed StructuralFoundation.KindIsSlab
- Element.OverrideTransparencyInView now returns the list of elements

###Deprecated nodes:
- Dispatch - Use List.FilterByBoolMask instead
- StructuralFoundation.FootingType - Use Element.Type instead

###Renamed nodes:
- Renamed List.ContainsOutOfPlanePoints to PointSequence.ContainsOutOfPlanePoints
- Renamed Point.GreatestDistanceInSequence to PointSequence.GreatestDistanceToPoint

##0.75.14

###New nodes:
- Element.Type (LinkedFile)
- String.BinaryToDecimal
- List.CountOccurences
- List.FromString

###Improvements/Changes:
- List.GroupListOfListsByKey now first sorts by key before grouping
- List.CountBooleanSequences now counts sequences of true *and* false at the same time
- Recategorized some nodes

###Renamed nodes:
- Renamed List.FilterSublistsByLength to List.FilterBySublistLength
- Renamed List.SublistByLengths to List.ChopByLengths
- Renamed List.FillSublist to List.RepeatItemsByLengths
- Renamed Binary.ToDecimal to List.BinaryToDecimal
- Renamed Line.ClosedLoopThroughPoints to Curve.ClosedLoopThroughPoints
- Renamed List.FindInSublists to List.SublistsContain

##0.75.13

###New nodes:
- All Intersecting Elements of Category
- BoundingBox.PerimeterCurvesByNormal
- BoundingBox.PerimeterCurvesOnPlane
- BoundingBox.ByNestedListOfElements
- RevisionCloud.FromCurves
- RevisionCloud.FromNestedListOfElements
- RevitBoundingBox.FromDynamoBoundingBox
- View.Plane

###Improvements/Changes:
- Renamed Element.BoundingBox to BoundingBox.ByElement
- BoundingBox.ByElement now also returns a Dynamo bounding box
- BoundingBox.ByElement now takes a view as an input (previously only active view possible)

##0.75.12

###Improvements:
- Small correction in TextElement.SetText

##0.75.11

###New nodes:
- TextElement.SetText
- TextElement.Text

###Improvements:
- Element.Location now also returns the location of TextNotes and Revit XYZs

##0.75.10

###New nodes:
- Time.EvaluateLapTimes
- Time.LapTime
- Wall.Flip

###Deprecated nodes:
- CurtainSystem.Type - use Element.Type instead
- Dimension.Type - use Element.Type instead
- Floor.Type - use Element.Type instead
- Roof.Type - use Element.Type instead

##0.75.9

###New nodes:
- Element.Name (Universal)
- Element.SetWorkset
- Element.Workset

###Improvements/Changes:
- Renamed Element.MaterialParameterByCategory to Element.SetMaterialParameterByCategory
- All Elements Of Name now uses the Element.Name (Universal) node
- Room.Boundaries now retrieves the boundaries based on the area computation settings of the current document

##0.75.8

###New nodes:
- Element.Group
- Element.MaterialParameterByCategory
- Group.Members

##0.75.7

###New nodes:
- Level.Plane
- Point.RoundDownToPrecision
- Point.RoundToPrecision
- Point.RoundUpToPrecision
- UV.RoundDownToPrecision
- UV.RoundToPrecision
- UV.RoundUpToPrecision

##0.75.6

###New nodes:
- Element.ElevationOfHostLevel

###Improvements:
- Element.Inserts now also returns correct list structure when no inserts are present

##0.75.5

###New nodes:
- AreaSeparator.FromCurve
- CurtainSystem.ByFace
- RevitFaceReference.FromDynamoSurface
- Wall.ByFace
- WallLocationLine.CoreCenterline
- WallLocationLine.CoreExterior
- WallLocationLine.CoreInterior
- WallLocationLine.FinishFaceExterior
- WallLocationLine.FinishFaceInterior
- WallLocationLine.WallCenterline

###Improvements:
- Document.ProjectPosition now outputs lengths instead of doubles
- List.ReplaceItemAtIndex now takes a list of indices
- Buckyball.ByOriginAndRadius now returns separate lists for hexagonal and pentagonal surfaces
- Recategorized and relabeled some nodes (plus some changes in node descriptions)

###Fixes:
- Repaired StructuralFoundation.KindIsIsolated, StructuralFoundation.KindIsSlab & StructuralFoundation.KindIsWallFooting
- Buckyball.ByOriginAndRadius now returns correct list of up vectors

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